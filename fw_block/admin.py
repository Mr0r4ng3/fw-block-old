from django.contrib import admin
from fw_block.models import Firewall, IpAddress, ProtectedNetworks


@admin.register(Firewall)
class FirewallAdmin(admin.ModelAdmin):
    pass


@admin.register(IpAddress)
class IpAddressAdmin(admin.ModelAdmin):
    pass


@admin.register(ProtectedNetworks)
class ProtectedNetworksAdmin(admin.ModelAdmin):
    pass
