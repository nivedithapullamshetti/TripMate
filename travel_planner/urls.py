from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    # ADMIN
    path(
        'admin/',
        admin.site.urls
    ),


    # HOME
    path(
        '',
        views.home,
        name='home'
    ),


    # LOGIN / REGISTER
    path(
        'accounts/',
        views.accounts,
        name='accounts'
    ),


    # USER HOME
    path(
        'userhome/',
        views.userhome,
        name='userhome'
    ),


    # LOGOUT
    path(
        'logout/',
        views.logout_user,
        name='logout'
    ),


    # DASHBOARD
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),


    # PLAN TRIP
    path(
        'trips/',
        views.trips,
        name='trips'
    ),


    # SCHEDULE
    path(
        'schedules/',
        views.schedules,
        name='schedules'
    ),


    # SAVED TRIPS
    path(
        'mytrips/',
        views.mytrips,
        name='mytrips'
    ),


    # EXPENSES
    path(
        'expenses/',
        views.expenses,
        name='expenses'
    ),


    # DESTINATIONS
    path(
        'destinations/',
        views.destinations,
        name='destinations'
    ),


    # WEATHER
    path(
        'weather/',
        views.weather,
        name='weather'
    ),


    # REST API
    path(
        'tripapi/',
        views.trip_api,
        name='tripapi'
    ),

]