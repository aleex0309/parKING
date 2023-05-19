from django import forms
from .models import Reservation, University, Parking, ParkingSpot, Vehicle

class ReservationForm(forms.ModelForm):
    university = forms.ModelChoiceField(queryset=University.objects.all())
    parking = forms.ModelChoiceField(queryset=Parking.objects.none())
    parking_spot = forms.ModelChoiceField(queryset=ParkingSpot.objects.none())

    class Meta:
        model = Reservation
        fields = ['vehicle', 'date', 'university', 'parking', 'parking_spot']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'university' in self.data:
            university_id = self.data.get('university')
            self.fields['parking'].queryset = Parking.objects.filter(university_id=university_id)
        elif self.instance.pk:
            self.fields['parking'].queryset = self.instance.university.parking_set.all()

        if 'parking' in self.data and 'vehicle' in self.data:
            parking_id = self.data.get('parking')
            vehicle_id = self.data.get('vehicle')
            vehicle_type = Vehicle.objects.get(id=vehicle_id).type
            self.fields['parking_spot'].queryset = ParkingSpot.objects.filter(parking_id=parking_id, type=vehicle_type)
        elif self.instance.pk:
            self.fields['parking_spot'].queryset = self.instance.parking.parkingspot_set.all()

    class Media:
        js = ('reservation_form.js',)

class NewCarForm(forms.ModelForm):
    university = forms.ModelChoiceField(queryset=University.objects.all())
    parking = forms.ModelChoiceField(queryset=Parking.objects.none())
    parking_spot = forms.ModelChoiceField(queryset=ParkingSpot.objects.none())

    class Meta:
        model = Vehicle
        fields = ['plate', 'type', 'emissions', 'user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    class Media:
        js = ('new_car_form.js',)