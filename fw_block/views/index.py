from django.http import HttpResponse, HttpRequest
from django.views import View
from django.shortcuts import render
from fw_block.forms import SearchForm
from fw_block.models.ip import IpAddress


class Index(View):

    def get(self, request: HttpRequest) -> HttpResponse:

        form = SearchForm()
        ips = IpAddress.objects.filter(blocked__is_blocked=True).distinct()

        context = {
            "form": form,
            "ips": ips,
        }

        return render(request, "pages/index.html", context)
