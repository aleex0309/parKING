from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404, HttpResponseForbidden, JsonResponse
from web.models import University, Parking, ParkingSpot, TYPES, Reservation, VehicleUser, Vehicle
from .forms import ReservationForm, NewCarForm
from django.contrib.auth.decorators import login_required
import ambiental_type
from django.utils import timezone
from datetime import datetime, timedelta
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
    car_spots = ParkingSpot.objects.filter(
        parking=id_parking, type=TYPES[1][1])
    motorbike_spots = ParkingSpot.objects.filter(
        parking=id_parking, type=TYPES[0][1])
    return render(request, "web/parking.html", {"parking": parking, "spots": spots, "count_cars": len(car_spots), "count_motorbikes": len(motorbike_spots)})


@login_required
def dashboard(request: HttpRequest):
    user = request.user

    # Check if authenticated
    if not user.is_authenticated:
        return HttpResponseForbidden(
            "You need to be logged in to use this feature")

    reservations = Reservation.objects.filter(user=user)

    active_list = list()

    for reservation in reservations:
        active_list.append(reservation.date < timezone.now()
                           and timezone.now() < reservation.date_fi)

    active = zip(active_list, reservations)

    vehicleUser = VehicleUser.objects.filter(user=user)
    vehicles = [vu.vehicle for vu in vehicleUser]

    return render(request, "web/dashboard.html",
                  {"user": user, "reservations": reservations, "vehicles": vehicles, "active": active, "time": timezone.now()})


@login_required
def delete_vehicle(request: HttpRequest, id_vehicle):
    user = request.user

    # Check if a vehicle is owned by the user
    vehicle_user = VehicleUser.objects.get(user=user, vehicle=id_vehicle)
    if not vehicle_user:
        raise HttpResponseForbidden("")

    vehicle_user.delete()
    return redirect("dashboard")


@login_required
def add_time(request: HttpRequest, id_reserve):
    user = request.user

    active_reserve = Reservation.objects.get(user=user, id=id_reserve)
    if not active_reserve:
        raise HttpResponseForbidden("")

    active_reserve.date_fi = active_reserve.date_fi + timedelta(minutes=15)
    active_reserve.save()
    return redirect("dashboard")


@login_required
def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('dashboard')
    else:
        form = ReservationForm()

    return render(request, 'web/reserve.html', {'form': form})

@login_required
def new_car(request):
    if request.method == 'POST':
        form = NewCarForm(request.POST)
        if form.is_valid():
            new_car = form.save(commit=False)
            if not Vehicle.objects.filter(plate = new_car.plate):
                new_car.save()
            else:
                new_car = Vehicle.objects.get(plate = new_car.plate)
            if not VehicleUser.objects.filter(user = request.user, vehicle = new_car):
                VehicleUser.objects.create(user = request.user, vehicle = new_car)
            return redirect('dashboard')

    else:
        form = NewCarForm()
    
    return render(request, 'web/new_car.html', {'form': form})

def get_vehicle_label(request):
    plate = request.GET.get('plate')
    label = ambiental_type.main(plate)
    return JsonResponse({'label' : label})
    # Parkings for each university


def get_parkings_by_university(request):
    university_id = request.GET.get('university_id')

    if university_id:
        parkings = Parking.objects.filter(
            university_id=university_id).values('id', 'description')
        return JsonResponse(list(parkings), safe=False)
    else:
        return JsonResponse({'error': 'University ID not provided.'})


def get_parking_spots(request):
    parking_id = request.GET.get('parking_id')
    vehicle_type = request.GET.get('vehicle_type')

    if parking_id and vehicle_type:
        parking_spots = ParkingSpot.objects.filter(
            parking_id=parking_id, type=vehicle_type).values('id')
        return JsonResponse(list(parking_spots), safe=False)
    else:
        return JsonResponse({'error': 'Parking ID or vehicle type not provided.'})


def get_vehicle_type(request):
    vehicle_id = request.GET.get('vehicle_id')
    if vehicle_id:
        try:
            vehicle = Vehicle.objects.get(id=vehicle_id)
            vehicle_type = vehicle.type
            return JsonResponse({'vehicle_type': vehicle_type})
        except Vehicle.DoesNotExist:
            return JsonResponse({'error': 'Vehicle not found'}, status=404)
    else:
        return JsonResponse({'error': 'Vehicle ID not provided'}, status=400)
