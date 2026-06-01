from django.shortcuts import render

def destinations_home(request):
    return render(request, 'destinations.html')