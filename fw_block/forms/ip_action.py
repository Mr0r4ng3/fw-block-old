from django import forms
from fw_block.models import Firewall


def get_firewalls_choices():

    return [(f.id, f.name) for f in Firewall.objects.all()]


class IpActionForm(forms.Form):

    ip = forms.GenericIPAddressField(
        required=True,
        error_messages={
            "invalid": "Dirección IP inválida.",
            "required": "Es necesario rellenar el campo de IP.",
        },
    )

    firewalls = forms.MultipleChoiceField(
        required=True,
        choices=get_firewalls_choices,
        error_messages={"required": "Es necesario seleccionar al menos 1 firewall."},
    )
    reason = forms.CharField(
        required=True,
        error_messages={"required": "Es necesario rellenar el campo de motivo."},
    )
