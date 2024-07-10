from django.db import models


class IpAddress(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    asn = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)

    def __str__(self):
        return self.ip
