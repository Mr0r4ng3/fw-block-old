from ipaddress import AddressValueError, IPv4Address
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from fw_block.models import IpAddress, Firewall


class Unblock(PermissionRequiredMixin, View):

    permission_required = "fw_block.can_unblock"

    def get(self, request: HttpRequest, ip: str) -> HttpResponse:

        try:

            IPv4Address(ip)

        except AddressValueError:

            messages.error(request, "Invalid IP address")

            return redirect("index")

        ip_model = get_object_or_404(IpAddress, ip=ip)

        context = {
            "ip": ip_model,
            "firewalls": ip_model.blocked_in_firewalls,
        }

        return render(request, "pages/unblock.html", context)

    def post(self, request: HttpRequest, ip: str) -> HttpResponse:

        firewalls_id = request.POST.getlist("firewalls")

        ip_model = get_object_or_404(IpAddress, ip=ip)
        failed_firewalls = 0
        succesful_firewalls = 0

        for id in firewalls_id:

            firewall = get_object_or_404(Firewall, id=id)

            if not firewall.unblock(ip_model):
                failed_firewalls += 1
                continue

            succesful_firewalls += 1

        if succesful_firewalls > 0:

            messages.info(
                request,
                f"Se desbloqueo exitosamente la IP en {succesful_firewalls} firewalls",
            )

        if failed_firewalls > 0:

            messages.error(
                request,
                f"No se pudo desbloquear la IP en {failed_firewalls} firewalls",
            )

        return redirect("index")
