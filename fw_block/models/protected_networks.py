from ipaddress import IPv4Network
from django.db import models


class ProtectedNetworks(models.Model):

    class Meta:
        app_label = "fw_block"

    cidr = models.CharField(max_length=18)

    def to_ipv4_network(self):

        return IPv4Network(self.cidr)

    def __str__(self):

        return self.cidr
