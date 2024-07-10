from django.contrib import admin
from fw_block.models import Firewall, IpAddress, Blocked


@admin.register(Firewall)
class FirewallAdmin(admin.ModelAdmin):
    pass


@admin.register(IpAddress)
class IpAddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Blocked)
class BlockedAdmin(admin.ModelAdmin):
    pass
