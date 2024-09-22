from django.shortcuts import render
from django.views import View
from core.models import Owner, Car, VehicleStatus
from django.http.response import HttpResponse



class VehiclePageView(View):
    
    def get(self, request, data):
        exists = Owner.objects.filter(rfid=data).exists()
        if exists:
            owner = Owner.objects.get(rfid=data)
            car = Car.objects.filter(owner=owner).first()
            # status = VehicleStatus.objects.get(car=car)
            context = {
                "owner": owner,
                "car": car,
                        # "status": status
            }
            return render(request, "vehicle_view.html", context)
        else:
            return render(request, "owner_not_exists.html", {})