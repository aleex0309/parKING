from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class University(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'


class UserUniversity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.user)+"@"+str(self.university)}'


TYPES = [('motorbike', 'motorbike'), ('car', 'car'), ("van", 'van')]


class Vehicle(models.Model):
    plate = models.CharField(max_length=128)
    type = models.CharField(choices=TYPES, max_length=50)
    emissions = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.plate}'


class VehicleUser(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.vehicle)+"@"+str(self.user)}'


class Parking(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.university}#{self.description}'


class ParkingSpot(models.Model):
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    type = models.CharField(choices=TYPES, max_length=50)

    def __str__(self):
        return f'{self.id}'


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateTimeField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.id}'
