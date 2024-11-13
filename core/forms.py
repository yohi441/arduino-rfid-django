from django import forms
from core.models import Car, Owner, VehicleStatus


class VehicleRegisterForm(forms.Form):
    tailwind_class = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
    # owner
    first_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": tailwind_class})
    )
    last_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": tailwind_class})
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": tailwind_class}))
    phone_number = forms.CharField(
        max_length=15, widget=forms.TextInput(attrs={"class": tailwind_class})
    )
    profile_photo = forms.ImageField(
        required=False, widget=forms.FileInput(attrs={"class": tailwind_class})
    )

    # car
    make = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": tailwind_class})
    )
    model = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": tailwind_class})
    )
    license_plate = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": tailwind_class})
    )
    photo = forms.ImageField(
        required=False, widget=forms.FileInput(attrs={"class": tailwind_class})
    )


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = [
            "rfid",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "profile_photo",
        ]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["make", "model", "license_plate", "photo", "color"]


class VehicleStatusForm(forms.ModelForm):
    class Meta:
        model = VehicleStatus
        fields = ["status", "description"]
