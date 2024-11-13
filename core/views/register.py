from django.shortcuts import render, redirect
from django.views import View
from core.models import Owner, Car, VehicleStatus, VehicleLog
from django.http.response import HttpResponse
from core.forms import VehicleRegisterForm
from core.models import SerialPortConfiguration
from core.utils import list_serial_ports
from django.db import IntegrityError
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


def extract_unique_field_name(error_message):
    # Logic to extract field name from the error message
    # This might vary based on your database backend
    # Example for SQLite
    if "UNIQUE constraint failed: core" in error_message:
        return error_message.split(".")[-1].strip()
    return "Unknown field"


class RegisterPageView(LoginRequiredMixin, View):
    def get(self, request):
        port = SerialPortConfiguration.objects.first()
        list_of_ports = list_serial_ports()
        context = {"list_of_ports": list_of_ports, "current_port": port.port}
        return render(request, "register.html", context)

    def post(self, request):
        selected_port = request.POST.get("selected_port")
        port = SerialPortConfiguration.objects.first()
        port.port = selected_port
        port.save()
        list_of_ports = list_serial_ports()
        context = {"list_of_ports": list_of_ports, "current_port": port.port}
        return render(request, "check_in.html", context)


class RegisterDetailView(View):
    def owner_data_save(self, data):
        owner = Owner.objects.create(
            rfid=data.get("rfid"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            phone_number=data.get("phone_number"),
            profile_photo=data.get("profile_photo"),
        )
        owner.save()
        return owner

    def car_data_save(self, data, owner, vehicle_status):
        car = Car.objects.create(
            owner=owner,
            make=data.get("make"),
            model=data.get("model"),
            license_plate=data.get("license_plate"),
            photo=data.get("photo"),
            vehicle_status=vehicle_status,
        )
        car.save()
        return car

    def get(self, request, data):
        form = VehicleRegisterForm()
        exists = Owner.objects.filter(rfid=data).exists()
        if exists:
            return render(request, "owner_exist.html")

        return render(request, "register_view.html", {"form": form, "data": data})

    def post(self, request, data):
        form = VehicleRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Extract the cleaned data
                first_name = form.cleaned_data["first_name"]
                last_name = form.cleaned_data["last_name"]
                email = form.cleaned_data["email"]
                phone_number = form.cleaned_data["phone_number"]
                profile_photo = form.cleaned_data["profile_photo"]
                make = form.cleaned_data["make"]
                model = form.cleaned_data["model"]
                license_plate = form.cleaned_data["license_plate"]
                photo = form.cleaned_data["photo"]

                owner = {
                    "rfid": data,
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "phone_number": phone_number,
                    "profile_photo": profile_photo,
                }
                car = {
                    "make": make,
                    "model": model,
                    "license_plate": license_plate,
                    "photo": photo,
                }
                with transaction.atomic():
                    owner_instance = self.owner_data_save(owner)
                    vs = VehicleStatus.objects.create()
                    car = self.car_data_save(
                        data=car, owner=owner_instance, vehicle_status=vs
                    )
                    VehicleLog.objects.create(car=car)
                messages.success(request, "Your data was saved successfully!")
            except IntegrityError as e:
                # Check if the error is related to a UNIQUE constraint
                if "UNIQUE constraint" in str(e):
                    # Extract the field name from the error message
                    # This example assumes the error message contains the field name
                    # Modify the logic based on your database backend's error message format
                    field_name = extract_unique_field_name(str(e))
                    error = f"Error: The field {field_name} must be unique"

                return render(
                    request,
                    "register_view.html",
                    {"form": form, "data": data, "error": error},
                )

            return redirect("owner-vehicle-list")
        else:
            return render(request, "register_view.html", {"form": form, "data": data})
