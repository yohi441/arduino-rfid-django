from django.contrib import admin
from core.models import Owner, Car, VehicleStatus


class OwnerModelAdmin(admin.ModelAdmin):
    pass

class CarModelAdmin(admin.ModelAdmin):
    pass

class VehicleStatusAdmin(admin.ModelAdmin):
    pass


admin.site.register(Owner, OwnerModelAdmin)
admin.site.register(Car, CarModelAdmin)
admin.site.register(VehicleStatus, VehicleStatusAdmin)