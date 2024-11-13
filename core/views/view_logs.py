from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import VehicleLog, Owner, Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class OwnerLogsView(LoginRequiredMixin, View):
    def get(self, request, pk):
        owner = Owner.objects.get(pk=pk)
        car = Car.objects.get(owner=owner)
        vehicle_logs = VehicleLog.objects.filter(car=car)
        date = request.GET.get("date")
        if date:
            vehicle_logs = vehicle_logs.filter(time_in__date=date)

        # Set up pagination
        paginator = Paginator(vehicle_logs, 10)  # Show 10 logs per page
        page_number = request.GET.get("page")

        try:
            logs_paginated = paginator.page(page_number)
        except PageNotAnInteger:
            logs_paginated = paginator.page(1)
        except EmptyPage:
            logs_paginated = paginator.page(paginator.num_pages)
        context = {"logs": logs_paginated, "owner": owner}
        return render(request, "logs.html", context)
