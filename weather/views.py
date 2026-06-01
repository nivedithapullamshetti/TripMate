from django.shortcuts import render

def weather_home(request):
    return render(request, 'weather.html')