from django.db import models


class Actions(models.TextChoices):

    block = "block"
    unblock = "unblock"


class BlockedLogs(models.Model):
    ip = models.ForeignKey("IpAddress", on_delete=models.CASCADE)
    firewall = models.ForeignKey("Firewall", on_delete=models.CASCADE)
    action = models.CharField(max_length=7, choices=Actions, default=Actions.block)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.datetime} - {self.user.username} - {self.action} - {self.ip.ip} - {self.firewall.name}"
