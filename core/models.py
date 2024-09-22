from django.db import models


class SerialPortConfiguration(models.Model):
    port = models.CharField(blank=True, null=True, max_length=10)


class Owner(models.Model):
    """Model to represent a car owner."""
    rfid = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Car(models.Model):
    """Model to represent a car."""
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='cars')
    make = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    license_plate = models.CharField(max_length=15, unique=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='car_photos/', blank=True, null=True)
    vehicle_status = models.OneToOneField('VehicleStatus', on_delete=models.CASCADE, related_name='car', null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"
    
class VehicleStatus(models.Model):
    """Mode to represent a vehicle status"""
    status = models.CharField(default="out", max_length=50, choices=[('in', 'In'), ('out', 'Out')], blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Vehicle Status"

    
    def __str__(self):
        return self.status