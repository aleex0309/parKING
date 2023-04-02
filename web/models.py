from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Reservation(models.Model):
    pass


class University(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class UserUniversity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.user)+"@"+str(self.university)


class Vehicle(models.Model):
    TYPES = [('motorbike', 'motorbike'), ('car', 'car'), ("van", 'van')]

    plate = models.CharField(max_length=128)
    type = models.CharField(choices=TYPES, max_length=50)
    emissions = models.CharField(max_length=1)

    def __str__(self) -> str:
        return self.plate


class VehicleUser(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.vehicle)+"@"+str(self.user)


class ParkingSpot(models.Model):
    pass


class Parking(models.Model):
    pass
