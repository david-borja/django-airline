from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.add(flight) # this abstraction is equivalent to adding a new row into a table
        
        # reverse takes the name of a particular view, and gives its url.
        # WARNING: args must be structured as a tuple!! so the end comma is crucial!
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
