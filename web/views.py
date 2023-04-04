from django.shortcuts import render
from django.http import HttpResponse, Http404
from web.models import University, Parking, ParkingSpot, TYPES

# Create your views here.

def home(request):
    universities = University.objects.all()
    return render(request, "web/index.html", {"universities":universities})

def university(request, id_university):
    try:
        university = University.objects.get(id=id_university)
    except University.DoesNotExist:
        raise Http404("University does not exist")
    parkings = Parking.objects.filter(university=university)
    return render(request, "web/university.html", {"university":university, "parkings":parkings})

def parking(request, id_university, id_parking):
    try: 
        parking = Parking.objects.get(id=id_parking, university=id_university)
    except Parking.DoesNotExist:
        raise Http404("Parking does not exist")
    spots = ParkingSpot.objects.filter(parking=id_parking)
    car_spots = ParkingSpot.objects.filter(parking=id_parking, type=TYPES[1][1])
    motorbike_spots = ParkingSpot.objects.filter(parking=id_parking, type=TYPES[0][1])
    return render(request, "web/parking.html", {"parking":parking, "spots":spots, "count_cars":len(car_spots), "count_motorbikes":len(motorbike_spots)})