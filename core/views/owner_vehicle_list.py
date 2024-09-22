from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from core.models import Owner, Car, VehicleStatus
from django.http.response import HttpResponse
from core.forms import VehicleRegisterForm, OwnerForm, CarForm, VehicleStatusForm

class OwnerVehicleListView(View):
    
    def get(self, request):
        cars = Car.objects.all()
        # owners = Owner.objects.prefetch_related(
        #     'cars__vehicle_status'
        # ).all()
        context = {
            "cars": cars
        }
        return render(request, "owner_vehicle_list.html", context)
    
class OwnerVehicleDetailView(View):

    def get(self, request, pk, car_pk):
            owner = get_object_or_404(Owner, pk=pk)
            car = get_object_or_404(Car, pk=car_pk)
            car_img_url = False
            owner_img_url = False
            if car.photo:
                car_img_url = True
            if owner.profile_photo:
                owner_img_url = True

            context = {
                "owner": owner,
                "car": car,
                "car_img_url": car_img_url,
                "owner_img_url" :owner_img_url,
                "owner_pk": pk,
                "car_pk": car_pk
            }

            return render(request, 'owner_vehicle_detail.html', context)

    def post(self, request, pk, car_pk):
        owner = get_object_or_404(Owner, pk=pk)
        owner_form = OwnerForm(request.POST, request.FILES, instance=owner)
        
        # Initialize car and status forms with POST data
        car_forms = {}
        status_forms = {}
        for car in owner.cars.all():
            car_form = CarForm(request.POST, request.FILES, instance=car)
            status_form = VehicleStatusForm(request.POST, instance=car.vehicle_status)
            car_forms[car.pk] = car_form
            status_forms[car.pk] = status_form

        if owner_form.is_valid():
            owner_form.save()

            all_forms_valid = True
            for car in owner.cars.all():
                car_form = car_forms[car.pk]
                status_form = status_forms[car.pk]
                
                if car_form.is_valid():
                    car_form.save()
                else:
                    all_forms_valid = False

                if status_form.is_valid():
                    status_form.save()
                else:
                    all_forms_valid = False

            if all_forms_valid:
                return redirect('owner-vehicle-detail', pk=owner.pk)

        # If form validation fails, render the template with forms and errors
        car_details = []
        for car in owner.cars.all():
            status = car.vehicle_status
            car_details.append({
                'car': car,
                'status': status
            })

        context = {
            'owner': owner,
            'car_details': car_details,
            'owner_form': owner_form,
            'car_forms': car_forms,
            'status_forms': status_forms
        }

        return render(request, 'owner_vehicle_detail.html', context)
