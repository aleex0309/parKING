from django import forms
from web.models import TYPES, ParkingSpot, Parking, University, VehicleUser, Reservation
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

class ReservationForm(forms.Form):
    class Meta:
        model = Reservation
        fields = ['user', 'vehicle', 'parking_spot']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if not User.is_authenticated:
            return HttpResponseForbidden(
            "You need to be logged in to use this feature")
        self.fields['vehicle'].queryset = VehicleUser.objects.filter(user=self.user)
        self.fields['parking_spot'].queryset = ParkingSpot.objects.filter(free=True)
        
