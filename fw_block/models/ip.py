from django.db import models

from fw_block.models.blocked import Blocked


class IpAddress(models.Model):

    class Meta:
        app_label = "fw_block"

    ip = models.GenericIPAddressField(unique=True, db_index=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    asn = models.CharField(max_length=100)
    organization = models.CharField(max_length=100, blank=True, null=True)

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

        return self.blocked_in.filter(blocked__is_blocked=True, blocked__ip=self.id)
