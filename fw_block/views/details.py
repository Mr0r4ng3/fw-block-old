from ipaddress import AddressValueError, IPv4Address
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from fw_block.models import IpAddress


class Details(PermissionRequiredMixin, View):

    permission_required = "fw_block.view_ipaddress"
    http_method_names = ["get"]

    def get(self, request: HttpRequest, ip: str) -> HttpResponse:

        try:

            IPv4Address(ip)

        except AddressValueError:

            messages.error(request, "Dirección IP inválida", extra_tags="danger")

            return redirect("index")

        ip_model = get_object_or_404(IpAddress, ip=ip)

        context = {
            "ip": ip_model,
            "firewalls": ip_model.blocked_in_firewalls,
        }

        return render(request, "pages/details.html", context)
