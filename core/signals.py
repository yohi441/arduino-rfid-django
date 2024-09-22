from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Car, VehicleStatus

@receiver(post_delete, sender=Car)
def post_delete_handler(sender, instance, **kwargs):
    instance.vehicle_status.delete()
    print(f'Post deleted')