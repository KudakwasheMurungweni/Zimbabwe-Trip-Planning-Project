from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('destinations/', views.destination_list, name='destination_list'),
    path('trips/', views.trip_list, name='trip_list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('book_trip/<int:trip_id>/', views.book_trip, name='book_trip'),
]