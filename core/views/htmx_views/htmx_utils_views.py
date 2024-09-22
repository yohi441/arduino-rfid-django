from django.shortcuts import render
from core.models import SerialPortConfiguration
from core.models import Owner, Car, VehicleStatus
from core.forms import OwnerForm, CarForm
from django.urls import reverse
import serial
from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponse
from django.contrib import messages

htmx_dir = "htmx_partials/"

def check_database(request, data):
    
    rfid = data.strip()
    exists = Owner.objects.filter(rfid=rfid).exists()
    if not exists:
        s = Owner.objects.create(rfid=rfid)
        s.save()
        print("make a owner data registration form")
    else:
        print("rfid exist in the database")
    return render(request, f"{htmx_dir}sample.html", {})

def get_rfid(request):
    port_config = SerialPortConfiguration.objects.first()
    port = port_config.port
    data = "no data found"
    ser = None
    try:
        ser = serial.Serial(port, 9600)
        data = ser.readline().decode('utf-8').strip()
        ser.close()
    except Exception as e:
        print("Invalid Serial Port", e)
    finally:
        if ser:
            ser.close()
    context = {
        "data": data
    }
    if data != "no data found":
        response =  JsonResponse({
            "message": "Redirecting"
        })
        redirect_url = reverse('register-rfid', args=[data])
        response['HX-Redirect'] = redirect_url 
        return response
    
    return render(request, f"{htmx_dir}rfid_partials.html", context)

def get_rfid_in_home(request):
    port_config = SerialPortConfiguration.objects.first()
    port = port_config.port
    data = "no data found"
    ser = None
    try:
        ser = serial.Serial(port, 9600)
        data = ser.readline().decode('utf-8').strip()
        ser.close()
    except Exception as e:
        pass
    finally:
        if ser:
            ser.close()

    context = {
        "data": data
    }
    if data != "no data found":
        response =  JsonResponse({
            "message": "Redirecting"
        })
        redirect_url = reverse('vehicle-detail-view', args=[data])
        response['HX-Redirect'] = redirect_url 
        return response
    
    return render(request, f"{htmx_dir}rfid_partials_home.html", context)

def get_vehicle_status(request, data):
    print(data)
    # split_uid = data.split(":")
    # rfid = split_uid[1].strip()
    # owner = Owner.objects.get(rfid=rfid)
    # car = Car.objects.get(owner=owner)
    # vehicle_status = VehicleStatus.objects.get(car=car)

    # context = {
    #     "owner" : owner,
    #     "car" : car,
    #     "vehicle_status": vehicle_status
    # }

    return render(request, f"{htmx_dir}check_vehicle_partials.html", {})


def get_form_owner_update(request, owner_pk, car_pk):
    owner = Owner.objects.get(id=owner_pk)
    if request.method == "GET":
        form = OwnerForm(instance=owner)
        return render(request, f"{htmx_dir}form_owner_update.html", {"form":form, "owner_pk": owner_pk, "car_pk": car_pk })
    elif request.method == "POST":
        form = OwnerForm(request.POST, request.FILES, instance=owner)
        if form.is_valid():
            form.save()
            response =  JsonResponse({
                "message": "Redirecting"
            })
            redirect_url = reverse('owner-vehicle-detail', args=[owner_pk, car_pk])
            response['HX-Redirect'] = redirect_url
            messages.success(request, "Owner Information Updated")
            return response
        return render(request, f"{htmx_dir}form_owner_update.html", {"form":form, "owner_pk": owner_pk, "car_pk": car_pk})
    
def get_form_car_update(request, owner_pk, car_pk):
    car = Car.objects.get(id=car_pk)
    if request.method == "GET":
        form = CarForm(instance=car)
        return render(request, f"{htmx_dir}form_car_update.html", {"form":form, "owner_pk": owner_pk, "car_pk": car_pk })
    elif request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            form.save()
            response =  JsonResponse({
                "message": "Redirecting"
            })
            redirect_url = reverse('owner-vehicle-detail', args=[owner_pk, car_pk])
            response['HX-Redirect'] = redirect_url
            messages.success(request, "Vehicle Information Updated")
            return response
        return render(request, f"{htmx_dir}form_car_update.html", {"form":form, "owner_pk": owner_pk, "car_pk": car_pk})
    
def update_status(request, status, car_pk):
    current_status = status
    car = Car.objects.get(id=car_pk)
    vs = VehicleStatus.objects.get(car=car)
    vs.status = status
    vs.save()
    car = Car.objects.get(id=car_pk)
    context = {
        "car": car
    }
   
    return render(request, f"{htmx_dir}update_button_partials_in.html", context)
   