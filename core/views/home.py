from django.shortcuts import render
from django.views import View
from core.utils import list_serial_ports
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import SerialPortConfiguration


class HomePageView(LoginRequiredMixin, View):
    login_url = 'accounts/login/'

    def get(self, request):
        port = SerialPortConfiguration.objects.first()
        list_of_ports = list_serial_ports()
        context = {
        "list_of_ports": list_of_ports,
        "current_port": port.port
        }
        return render(request, "check_in.html", context)
    
    def post(self, request):
        selected_port = request.POST.get("selected_port")
        port = SerialPortConfiguration.objects.first()
        port.port = selected_port
        port.save()
        list_of_ports = list_serial_ports()
        context = {
        "list_of_ports": list_of_ports,
        "current_port": port.port
        }
        return render(request, "check_in.html", context)