from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseForbidden
from web.models import University, Parking, ParkingSpot, TYPES, Reservation, VehicleUser, UserUniversity
from .forms import ReservationForm

# Create your views here.


def home(request):
    universities = University.objects.all()
    return render(request, "web/index.html", {"universities": universities})


def university(request, id_university):
    try:
        university = University.objects.get(id=id_university)
    except University.DoesNotExist:
        raise Http404("University does not exist")
    parkings = Parking.objects.filter(university=university)
    return render(request, "web/university.html", {"university": university, "parkings": parkings})


def parking(request, id_university, id_parking):
    try:
        parking = Parking.objects.get(id=id_parking, university=id_university)
    except Parking.DoesNotExist:
        raise Http404("Parking does not exist")
    spots = ParkingSpot.objects.filter(parking=id_parking)
    car_spots = ParkingSpot.objects.filter(parking=id_parking, type=TYPES[1][1])
    motorbike_spots = ParkingSpot.objects.filter(parking=id_parking, type=TYPES[0][1])
    return render(request, "web/parking.html", {"parking":parking, "spots":spots, "count_cars":len(car_spots), "count_motorbikes":len(motorbike_spots)})

def dashboard(request: HttpRequest):
    user = request.user

    # Check if authenticated
    if not user.is_authenticated:
        return HttpResponseForbidden(
            "You need to be logged in to use this feature")

    reservations = Reservation.objects.filter(user=user)

    vehicleUser = VehicleUser.objects.filter(user=user)
    vehicles = [vu.vehicle for vu in vehicleUser]

    return render(request, "web/dashboard.html",
                  {"user": user, "reservations": reservations, "vehicles": vehicles})


def delete_vehicle(request: HttpRequest, id_vehicle):
    user = request.user

    # Check if a vehicle is owned by the user
    vehicle_user = VehicleUser.objects.get(user=user, vehicle=id_vehicle)
    if not vehicle_user:
        raise HttpResponseForbidden("")

    vehicle_user.delete()
    return redirect("dashboard")


def reserve(request: HttpRequest):
    form = ReservationForm()
    if request.method =='POST':
        form = ReservationForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect("web/reserve.html")
    return render (request, "dashboard",{'form': form})

def load_parkings(request):
    university_id = request.GET.get('university_id')
    parkings = Parking.objects.filter(university_id=university_id).all()
    return render(request, 'web/parking_dropdown_list.html', {'parking': parkings})
