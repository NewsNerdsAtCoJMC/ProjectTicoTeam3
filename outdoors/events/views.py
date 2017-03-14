from django.shortcuts import render
from .models import Location

def index(request):
    locations = Location.objects.all()
    context = { 'locations': locations}
    return render(request, 'outdoors/index.html', context)

def trails(request):
    locations = Location.objects.all()
    context = { 'locations': locations}
    return render(request, 'outdoors/trails.html', context)

def traffic(request):
    locations = Location.objects.all()
    context = { 'locations': locations}
    return render(request, 'outdoors/traffic.html', context)

def test(request):
    locations = Location.objects.all()
    context = { 'locations': locations}
    return render(request, 'outdoors/test.html', context)
