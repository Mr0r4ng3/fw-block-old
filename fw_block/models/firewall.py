from django.db import models


class Firewall(models.Model):
    name = models.CharField(max_length=100)
    ip = models.GenericIPAddressField(unique=True)
    context = models.CharField(max_length=100)

    blocked_ips = models.ManyToManyField(
        "IpAddress", related_name="blocked_in", through="Blocked"
    )

    def __str__(self):
        return f"{self.name} - {self.context} ({self.ip})"
