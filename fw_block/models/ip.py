from django.db import models


class IpAddress(models.Model):

    class Meta:
        app_label = "fw_block"
        permissions = (("search_ipaddress", "Can search IPs"),)
        verbose_name = "Dirección IP"
        verbose_name_plural = "Direcciones IP"

    ip = models.GenericIPAddressField(unique=True, db_index=True, verbose_name="IP")
    country = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="País"
    )
    region = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Estado"
    )
    city = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Ciudad"
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    asn = models.CharField(max_length=100, blank=True, null=True)
    organization = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Organización"
    )

    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.ip

    def to_dict(self):
        return {
            "ip": self.ip,
            "country": self.country,
            "region": self.region,
            "city": self.city,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "asn": self.asn,
            "organization": self.organization,
        }

    @property
    def blocked_in_firewalls(self):

        return self.blocked_in.all()

    @property
    def blocked_in_firewalls_first_3(self):

        return self.blocked_in.all()[0:3]

    @property
    def blocked_in_firewalls_count(self) -> bool:

        return self.blocked_in.all().count()
