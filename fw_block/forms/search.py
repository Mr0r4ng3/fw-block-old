from ipaddress import AddressValueError, IPv4Address, IPv4Network
from django import forms
from fw_block import settings
from fw_block.services.ip_api_query import query_ip_in_api
from fw_block.models import IpAddress


def check_ip_in_protected_network(ip: str, protected_networks: list[str]) -> None:

    for protected_network in protected_networks:

        if IPv4Address(ip) in IPv4Network(protected_network):

            raise forms.ValidationError("IP Address in protected network")


class SearchForm(forms.Form):
    ip = forms.CharField(
        max_length=15,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "8.8.8.8"}),
        required=True,
    )

    model = None

    def clean_ip(self):

        ip = self.cleaned_data.get("ip")

        try:

            check_ip_in_protected_network(ip, settings.PROTECTED_NETWORKS)

        except AddressValueError:

            raise forms.ValidationError("Invalid IP address")

        return ip

    def query_ip(self) -> dict:
        ip = self.cleaned_data.get("ip")

        try:
            self.model = IpAddress.objects.get(ip=ip)

            print("Query from db")

            return self.model.to_dict()

        except IpAddress.DoesNotExist:

            data = query_ip_in_api(ip)

            print("Query from api")

            if data.get("error"):

                return data

            new_ip = IpAddress.objects.create(
                ip=data.get("ip"),
                country=data.get("country_name"),
                region=data.get("region"),
                city=data.get("city"),
                latitude=data.get("latitude"),
                longitude=data.get("longitude"),
                asn=data.get("asn"),
                organization=data.get("org"),
            )

            new_ip.save()

            return new_ip.to_dict()
