from django.contrib.gis.geos import Point
from django.shortcuts import render
from .models import Coordinates



def index(request):
    return render(request, "mapische/base.html")


def save_coordinates(request, long, lat):
    coor = Coordinates(pointer=Point(float(long), float(lat)))
    coor.save()
    return render(request, "mapische/base.html")


def return_coordinates(request):
    coords = Coordinates.objects.all()
    return render(request, "mapische/coords.html", {"coords": coords})