from django.contrib.auth import get_user_model
from django.db import migrations

def create_admin_user(apps, schema_editor):
    User = get_user_model()
    admin_user = User.objects.create_superuser(username='admin', password='admin', email='admin@example.com')

def create_university_and_parking_spot(apps, schema_editor):
    University = apps.get_model('web', 'University')
    Parking = apps.get_model('web', 'Parking')
    ParkingSpot = apps.get_model('web', 'ParkingSpot')
    
    university = University.objects.create(name='Universitat de Lleida')

    parking = Parking.objects.create(description='Campus Cappont', university=university)

    parking_spot = ParkingSpot.objects.create(type='Car', free=True, parking=parking)

class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),  # Add the previous migration file's name here
    ]

    operations = [
        migrations.RunPython(create_admin_user),
        migrations.RunPython(create_university_and_parking_spot),
    ]
