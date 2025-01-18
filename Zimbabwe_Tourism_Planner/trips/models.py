from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Destination(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)

    def __str__(self):
        return self.name

class Trip(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    number_of_days = models.IntegerField()
    activities = models.TextField()

    def __str__(self):
        return f"Trip to {self.destination.name} ({self.start_date} - {self.end_date})"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, default='Booked')

    def __str__(self):
        return f"Booking by {self.user.username} for {self.trip.destination.name}"