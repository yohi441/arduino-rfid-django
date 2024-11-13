from django.contrib import admin
from core.models import (
    Owner,
    Car,
    VehicleStatus,
    VehicleLog,
    SerialPortConfiguration,
    SiteInfo,
)
from django.contrib.auth.models import Group, User

# admin.py
from django.contrib import admin
from .models import SiteInfo

# Custom admin class to change the site name
class CustomAdminSite(admin.AdminSite):
    site_header = "Admin"  # Default header

    def each_context(self, request):
        context = super().each_context(request)
        try:
            site_info = SiteInfo.objects.first()  # Get the first SiteInfo object
            if site_info:
                self.site_header = (
                    site_info.name
                )  # Set the site header to the name in the database
        except SiteInfo.DoesNotExist:
            pass  # Handle the case where no SiteInfo exists
        return context


# Instantiate the custom admin site
admin_site = CustomAdminSite(name="custom_admin")

# Register your models with the custom admin site
# Example: admin_site.register(YourModel)


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


admin_site.register(SiteInfo, SiteInfoAdmin)
admin_site.register(Owner, OwnerModelAdmin)
admin_site.register(Car, CarModelAdmin)
admin_site.register(VehicleStatus, VehicleStatusAdmin)
admin_site.register(VehicleLog, VehicleLogAdmin)
admin_site.register(SerialPortConfiguration, SerialPortConfigurationAdmin)
admin_site.register(Group)
admin_site.register(User)
