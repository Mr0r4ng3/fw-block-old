from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from fw_block.forms import IpActionForm
from fw_block.models import IpAddress, Firewall
from fw_block.models import BlockedLogs
from fw_block.models.blocked_logs import Actions
from fw_block.views.utils import extract_errors


class Unblock(PermissionRequiredMixin, View):

    permission_required = "fw_block.can_unblock"
    http_method_names = ["post"]

    def post(self, request: HttpRequest) -> HttpResponse:

        form = IpActionForm(request.POST)

        if not form.is_valid():

            errors = extract_errors(form)

            for error in errors:

                messages.error(request, error["reason"], extra_tags="danger")

            return redirect("index")

        firewalls_id = form.cleaned_data["firewalls"]

        ip_model = get_object_or_404(IpAddress, ip=form.cleaned_data["ip"])
        failed_firewalls = 0
        succesful_firewalls = 0

        for id in firewalls_id:

            firewall = get_object_or_404(Firewall, id=id)

            if not firewall.unblock(ip_model):
                failed_firewalls += 1
                continue

            succesful_firewalls += 1

            BlockedLogs.objects.create(
                ip=ip_model,
                firewall=firewall,
                user=request.user,
                action=Actions.unblock,
                reason=form.cleaned_data["reason"],
                description=f'{ip_model.organization if ip_model.organization else ""}{", " + ip_model.country if ip_model.country else ""}',
            )

        if succesful_firewalls > 0:

            messages.info(
                request,
                f"Se desbloqueo exitosamente la IP en {succesful_firewalls} firewall{'s' if succesful_firewalls > 1 else ''}",
                extra_tags="success",
            )

            ip_model.is_blocked = (
                False
                if Firewall.objects.filter(blocked__ip=ip_model.id).count() == 0
                else True
            )
            ip_model.save()

        if failed_firewalls > 0:

            messages.error(
                request,
                f"No se pudo desbloquear la IP en {failed_firewalls} firewall{'s' if failed_firewalls > 1 else ''}",
                extra_tags="danger",
            )

        return redirect("index")
