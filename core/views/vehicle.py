from django.shortcuts import render
from django.views import View
from core.models import Owner, Car, VehicleStatus, VehicleLog
from django.http.response import HttpResponse
import serial
from core.models import SerialPortConfiguration
import time
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone


class VehiclePageView(LoginRequiredMixin, View):
    def get(self, request, data):
        exists = Owner.objects.filter(rfid=data).exists()

        if exists:
            owner = Owner.objects.get(rfid=data)
            car = Car.objects.filter(owner=owner).first()
            vl = VehicleLog.objects.filter(car=car).order_by("time_out").first()
            vs = VehicleStatus.objects.get(car=car)

            status = vs.status
            if status == "in":
                vs.status = "out"
            else:
                vs.status = "in"
            vs.save()
            if not vl.time_out:
                if vs.status == "in":
                    vl.time_in = timezone.now()
                if vs.status == "out":
                    vl.time_out = timezone.now()
            else:
                vl = VehicleLog.objects.create(car=car)
                if vs.status == "in":
                    vl.time_in = timezone.now()
            vl.save()

            context = {
                "owner": owner,
                "car": car,
                # "status": status
            }
            return render(request, "vehicle_view.html", context)
        else:
            return render(request, "owner_not_exists.html", {})
