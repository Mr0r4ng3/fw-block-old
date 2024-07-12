from django.forms import Form
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect, render
from fw_block.models.firewall import Firewall
from fw_block.forms import SearchForm
from django.utils.translation import gettext as _


def extract_errors(form: Form):

    errors = []

    for _, field in form.errors.as_data().items():

        for error in field:

            errors.append({"error": True, "reason": error.message})

    return errors


class Search(PermissionRequiredMixin, View):

    permission_required = "fw_block.search_ipadress"

    def get(self, request):

        if not request.GET.get("ip"):

            return redirect("index")

        searchForm = SearchForm(request.GET)

        if not searchForm.is_valid():

            errors = extract_errors(searchForm)

            for error in errors:

                messages.error(request, error["reason"], extra_tags="danger")

            return redirect("index")

        data = searchForm.query_ip()

        firewalls = Firewall.objects.exclude(
            blocked__is_blocked=True, blocked__ip=searchForm.model.id
        )

        if firewalls.count() == 0:

            messages.warning(
                request,
                "La dirección IP ya se encuentra bloqueada en todos los firewalls",
                extra_tags="default",
            )
            return redirect("index")

        if data.get("error"):

            messages.error(request, data["reason"], extra_tags="danger")
            return redirect("index")

        context = {"ip": data, "firewalls": firewalls}

        return render(request, "pages/search.html", context)
