from django.shortcuts import render
from django.views import View
from core.utils import list_serial_ports
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import SerialPortConfiguration, Owner


class ChangeRfidView(LoginRequiredMixin, View):
    login_url = "accounts/login/"

    def get(self, request, pk):
        port = SerialPortConfiguration.objects.first()
        list_of_ports = list_serial_ports()
        context = {"list_of_ports": list_of_ports, "current_port": port.port}
        return render(request, "change_rfid.html", context)


class ChangeRfidChangeView(LoginRequiredMixin, View):
    login_url = "accounts/login/"

    def get(self, request, data, pk):
        exists = Owner.objects.filter(rfid=data).exists()

        if exists:
            return render(request, "rfid_exists.html")
        owner = Owner.objects.get(pk=pk)
        owner.rfid = data
        owner.save()
        return render(request, "successful_change.html")
