from django.forms import Form
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect, render
from fw_block.models.firewall import Firewall
from fw_block.services.ip_api_query import query_ip_in_api
from fw_block.forms import SearchForm


def extract_errors(form: Form):

    errors = []

    for _, field in form.errors.as_data().items():

        for error in field:

            errors.append({"error": True, "reason": error.message})

    return errors


class Search(View):
    def get(self, request):

        if not request.GET.get("ip"):

            return redirect("index")

        searchForm = SearchForm(request.GET)

        if not searchForm.is_valid():

            errors = extract_errors(searchForm)

            for error in errors:

                messages.error(request, error["reason"])

            return redirect("index")

        data = searchForm.query_ip()

        firewalls = Firewall.objects.exclude(
            blocked__is_blocked=True, blocked__ip=searchForm.model.id
        )

        if firewalls.count() == 0:

            messages.warning(
                request, "La ip ya se encuentra bloqueada en todos los firewalls"
            )
            return redirect("index")

        if data.get("error"):

            messages.error(request, data["reason"])
            return redirect("index")

        context = {"ip": data, "firewalls": firewalls}

        return render(request, "pages/search.html", context)
