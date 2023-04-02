from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Reservation(models.Model):
    pass


class Univesity(models.Model):
    pass


# La classe usuari s'ha de fer diferent per temes de la autenticacio que ja te django
class CustomUser(AbstractUser):
    pass


class Vehicle(models.Model):
    pass


class ParkingSpot(models.Model):
    pass


class Parking(models.Model):
    pass
