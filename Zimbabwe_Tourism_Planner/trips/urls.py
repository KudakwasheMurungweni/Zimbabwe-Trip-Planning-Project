from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from trips import views


urlpatterns = [
     path('Home/', views.home, name='home'),
    path('destinations/', views.destination_list, name='destination_list'),
    path('destinations/<int:destination_id>/', views.destination_detail, name='destination_detail'),
   path('trips/', views.trip_list, name='trip_list'),
    path('trips/<int:trip_id>/', views.trip_detail, name='trip_detail'),
    path('trips/book/<int:trip_id>/', views.book_trip, name='book_trip'),  # Booking view

   path('login/', auth_views.LoginView.as_view(template_name='trips/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='trips/logged_out.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('book_trip/<int:trip_id>/', views.book_trip, name='book_trip'),
]