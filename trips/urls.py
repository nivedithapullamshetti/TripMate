from django.urls import path
from . import views

urlpatterns = [
    path('', views.trips_home, name='trips_home'),
]