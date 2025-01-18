from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from .models import Destination, Trip, Booking
from .forms import BookingForm


def home(request):
    return render(request, 'Home/home.html')

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/destination_list.html', {'destinations': destinations})

def destination_detail(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/destination_detail.html', {'destinations': destinations})


def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'trips/trip_list.html', {'trips': trips})

def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)  # Fetch the trip or raise 404 if not found
    return render(request, 'trips/trip_detail.html', {'trip': trip})

def custom_logout(request):
    logout(request)  # Log the user out
    return render(request, 'Home/logged_out.html')

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Use a named URL pattern for the home page
    else:
        form = AuthenticationForm()
    return render(request, 'Home/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Home/signup.html', {'form': form})

def book_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('trips/trip_list.html')  # Redirect to the trips list after booking
    else:
        form = BookingForm(initial={'trip': trip})
    return render(request, 'trips/book_trip.html', {'form': form, 'trip': trip})