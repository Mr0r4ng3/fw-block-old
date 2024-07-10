from datetime import datetime
from django.db import models
from fw_block import settings
from fw_block.models.blocked import Blocked
from fw_block.models.ip import IpAddress
from fw_block.services import AsaAPI


class Firewall(models.Model):

    class Meta:
        app_label = "fw_block"

    name = models.CharField(max_length=100)
    ip = models.GenericIPAddressField(unique=True)
    context = models.CharField(max_length=100)

    blocked_ips = models.ManyToManyField(
        "IpAddress", related_name="blocked_in", through="Blocked"
    )

    def __str__(self):
        return f"{self.name} - {self.context} ({self.ip})"

    def get_cli_url(self) -> str:

        return f"https://{self.ip}/api/cli?context={self.context}"

    def block(self, ip: IpAddress) -> bool:

        try:

            asa_service = AsaAPI(
                api_url=self.get_cli_url(),
                username=settings.FW_USER,
                password=settings.FW_PASSWORD,
            )

            if asa_service.block_ip(ip.ip):

                blocked = Blocked.objects.get(ip=ip, firewall=self)

                blocked.is_blocked = True
                blocked.blocked_at = datetime.now()
                blocked.unblocked_at = None
                blocked.save()

                return True

            return False

        except Blocked.DoesNotExist:

            self.blocked_ips.add(ip)

        return True

    def unblock(self, ip: IpAddress) -> bool:

        asa_service = AsaAPI(
            api_url=self.get_cli_url(),
            username=settings.FW_USER,
            password=settings.FW_PASSWORD,
        )

        if asa_service.unblock_ip(ip.ip):

            blocked = Blocked.objects.get(ip=ip, firewall=self)

            blocked.is_blocked = False
            blocked.unblocked_at = datetime.now()
            blocked.save()

            return True

        return False
