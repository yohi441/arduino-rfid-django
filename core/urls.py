
from django.urls import path, include
from .views.home import HomePageView
from .views.register import RegisterPageView, RegisterDetailView
from .views.htmx_views.htmx_utils_views import check_database, get_rfid, get_rfid_in_home, get_vehicle_status, get_form_owner_update, get_form_car_update, update_status, get_rfid_in_change
from .views.vehicle import VehiclePageView
from .views.owner_vehicle_list import OwnerVehicleListView, OwnerVehicleDetailView
from .views.view_logs import OwnerLogsView
from .views.change_rfid import ChangeRfidView, ChangeRfidChangeView
urlpatterns = [
    path('', HomePageView.as_view(), name="home-page"),
    path('register/', RegisterPageView.as_view(), name="register-page"),
    path("check-in/vehicle/<str:data>/", VehiclePageView.as_view() , name="vehicle-detail-view"),
    path('register/rfid/<str:data>/', RegisterDetailView.as_view(), name="register-rfid"),
    path('owner/vehicle/list/', OwnerVehicleListView.as_view(), name="owner-vehicle-list"),
    path("owner/vehicle/detail/<int:pk>/<int:car_pk>/", OwnerVehicleDetailView.as_view(), name="owner-vehicle-detail"),
    path("owner/logs/<int:pk>/", OwnerLogsView.as_view(), name="owner-logs"),
    path("change/existing/rfid/<int:pk>", ChangeRfidView.as_view(), name="change-rfid"),
    path("change/rfid/<str:data>/<int:pk>/", ChangeRfidChangeView.as_view(), name="rfid-view")
]

htmx_urlpatterns = [
    path("check-database/<str:data>/", check_database, name="check-database"),
    path("get-rfid/", get_rfid, name="get-rfid"),
    path("get-rfid-home/", get_rfid_in_home, name="get-rfid-home"),
    path("get-rfid-change/<int:pk>/", get_rfid_in_change, name="get-rfid-change"),
    path("status/<str:data>/", get_vehicle_status, name="status"),
    path("get-owner-form/<int:owner_pk>/<int:car_pk>/", get_form_owner_update, name="get-form-owner-update"),
    path("get-car-form/<int:owner_pk>/<int:car_pk>/", get_form_car_update, name="get-form-car-update"),
    path('update-status/<str:status>/<int:car_pk>/', update_status, name="update-status")
   
]

auth_url_patterns = [
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += htmx_urlpatterns
urlpatterns += auth_url_patterns


