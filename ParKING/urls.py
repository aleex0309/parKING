"""ParKING URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import web.views as wv
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wv.home, name='home'), 
    path('reserve/', wv.reserve, name='reserve'),
    path('api/parkings/', wv.get_parkings_by_university, name='api_parkings'),
    path('api/parking-spots/', wv.get_parking_spots, name='api_parking_spots'),
    path('api/vehicle-type/', wv.get_vehicle_type, name='api_vehicle_type'),
    path('university/<int:id_university>/', wv.university, name='parkings'),
    path('university/<int:id_university>/parking/<int:id_parking>', wv.parking, name='parkingSpots'),
    path("dashboard/", wv.dashboard, name="dashboard"),
    path("vehicle/delete/<int:id_vehicle>",
         wv.delete_vehicle, name="vehicle_delete"),
    path("reserve/add_time/<int:id_reserve>",
         wv.add_time, name="add_time"),
         
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'))
]