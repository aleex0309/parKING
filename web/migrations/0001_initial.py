# Generated by Django 4.2.1 on 2023-05-19 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

from django.contrib.auth import get_user_model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSpot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Motorbike', 'Motorbike'), ('Car', 'Car'), ('Van', 'Van')], max_length=50)),
                ('free', models.BooleanField(default=True)),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.parking')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=128)),
                ('type', models.CharField(choices=[('Motorbike', 'Motorbike'), ('Car', 'Car'), ('Van', 'Van')], max_length=50)),
                ('emissions', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='UserUniversity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.university')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('date_fi', models.DateTimeField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=8)),
                ('parking_spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.parkingspot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.vehicleuser')),
            ],
        ),
        migrations.AddField(
            model_name='parking',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.university'),
        ),
    ]