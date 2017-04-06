from django.shortcuts import render
from .models import Location, Event

def index(request):
    locations = Location.objects.all()
    context = { 'locations': locations}
    return render(request, 'outdoors/index.html', context)

def events_trails(request):
    events = Event.objects.all()
    locations = Location.objects.all()
    context = { 'events': events, 'locations':locations}
    return render(request, 'outdoors/events_trails.html', context)

def events_traffic(request):
    events = Event.objects.all()
    locations = Location.objects.all()
    context = { 'events': events, 'locations':locations}
    return render(request, 'outdoors/events_traffic.html', context)

def venues(request):
    locations = Location.objects.all()
    context = { 'locations': locations}
    return render(request, 'outdoors/venues.html', context)

def events(request):
    events = Event.objects.all()
    locations = Location.objects.all()
    context = { 'events': events, 'locations':locations}
    return render(request, 'outdoors/events.html', context)
