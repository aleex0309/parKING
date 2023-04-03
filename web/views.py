from django.shortcuts import render
from django.http import HttpResponse, Http404
from web.models import University, Parking

# Create your views here.

def home(request):
    universities = University.objects.all()
    return render(request, "web/index.html", {"universities":universities})

def university(request, id_university):
    try:
        university = University.objects.get(pk=id_university)
    except University.DoesNotExist:
        raise Http404("University does not exist")
    parkings = Parking.objects.filter(university=university)
    return render(request, "web/university.html", {"university":university, "parkings":parkings})