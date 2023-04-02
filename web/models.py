from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Reservation(models.Model):
    pass


class Univesity(models.Model):
    name = models.CharField(max_length=256)


# La classe usuari s'ha de fer diferent per temes de la autenticacio que ja te django
# AL FINAL UN USUARI NOMES PODRA SER DE UNA UNIVERSITAT
# Al fer extend de abstract user ja hi han els seguents camps creats
# username, first_name, last_name, email, is_staff, is_active, date_joined, password, get_full_name(), get_short_name()
class CustomUser(AbstractUser):
    university = models.ForeignKey(Univesity, on_delete=models.CASCADE())


class Vehicle(models.Model):
    pass


class ParkingSpot(models.Model):
    pass


class Parking(models.Model):
    pass
