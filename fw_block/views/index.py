from django.http import HttpResponse, HttpRequest
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from fw_block.forms import SearchForm
from fw_block.models.ip import IpAddress


class Index(LoginRequiredMixin, View):

    http_method_names = ["get"]

    def get(self, request: HttpRequest) -> HttpResponse:

        form = SearchForm()
        ips = IpAddress.objects.filter(is_blocked=True)

        context = {
            "form": form,
            "ips": ips,
        }

        return render(request, "pages/index.html", context)
