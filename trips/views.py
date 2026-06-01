from django.shortcuts import render

def trips_home(request):
    return render(request, 'trips.html')