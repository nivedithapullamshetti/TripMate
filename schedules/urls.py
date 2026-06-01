from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedules_home, name='schedules_home'),
]