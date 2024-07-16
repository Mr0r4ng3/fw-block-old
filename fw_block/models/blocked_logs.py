from django.db import models


class Actions(models.TextChoices):

    block = "block", "Bloqueo"
    unblock = "unblock", "Desbloqueo"


class BlockedLogs(models.Model):

    class Meta:
        app_label = "fw_block"

        ordering = ["-datetime"]

    ip = models.ForeignKey("IpAddress", on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    firewall = models.ForeignKey("Firewall", on_delete=models.CASCADE)
    action = models.CharField(max_length=7, choices=Actions, default=Actions.block)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    reason = models.TextField(blank=True, default="")
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return f"{self.datetime} - {self.user.username} - {self.action} - {self.ip.ip} - {self.firewall.name}"
