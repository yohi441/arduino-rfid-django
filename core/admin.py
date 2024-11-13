from django.contrib import admin
from core.models import (
    Owner,
    Car,
    VehicleStatus,
    VehicleLog,
    SerialPortConfiguration,
    SiteInfo,
)

from .models import SiteInfo

admin.site.site_header = "SPMC"

class OwnerModelAdmin(admin.ModelAdmin):
    pass


class CarModelAdmin(admin.ModelAdmin):
    pass


class VehicleStatusAdmin(admin.ModelAdmin):
    pass


class VehicleLogAdmin(admin.ModelAdmin):
    pass


class SerialPortConfigurationAdmin(admin.ModelAdmin):
    pass


class SiteInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(SiteInfo, SiteInfoAdmin)
admin.site.register(Owner, OwnerModelAdmin)
admin.site.register(Car, CarModelAdmin)
admin.site.register(VehicleStatus, VehicleStatusAdmin)
admin.site.register(VehicleLog, VehicleLogAdmin)
admin.site.register(SerialPortConfiguration, SerialPortConfigurationAdmin)
