from ipaddress import IPv4Network
from django.db import models


class ProtectedNetworks(models.Model):

    class Meta:
        app_label = "fw_block"
        verbose_name = "Red protegida"
        verbose_name_plural = "Redes protegidas"

    cidr = models.CharField(max_length=18, verbose_name="CIDR")

    def to_ipv4_network(self):

        return IPv4Network(self.cidr)

    def __str__(self):

        return self.cidr
