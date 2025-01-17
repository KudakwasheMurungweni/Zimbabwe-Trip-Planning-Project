from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login
from .models import Destination, Trip, Booking
from .forms import BookingForm


def home(request):
    return render(request, 'trips/home.html')

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'trips/destination_list.html', {'destinations': destinations})

def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'trips/trip_list.html', {'trips': trips})

def custom_logout(request):
    logout(request)  # Log the user out
    return render(request, 'logged_out.html')

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page or wherever you prefer
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def book_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('trip_list')  # Redirect to the trips list after booking
    else:
        form = BookingForm(initial={'trip': trip})
    return render(request, 'book_trip.html', {'form': form, 'trip': trip})