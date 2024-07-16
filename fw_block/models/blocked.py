from django.db import models


class Blocked(models.Model):

    class Meta:
        app_label = "fw_block"

    ip = models.ForeignKey("IpAddress", on_delete=models.CASCADE)
    firewall = models.ForeignKey("Firewall", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.ip.ip} - {self.firewall.name}"
