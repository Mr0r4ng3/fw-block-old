from django.db import models


class Blocked(models.Model):
    ip = models.ForeignKey("IpAddress", on_delete=models.CASCADE)
    firewall = models.ForeignKey("Firewall", on_delete=models.CASCADE)
    is_blocked = models.BooleanField(default=True)

    blocked_at = models.DateTimeField(auto_now_add=True)
    unblocked_at = models.DateTimeField(null=True)
