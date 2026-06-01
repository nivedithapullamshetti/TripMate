from django.shortcuts import render

def schedules_home(request):
    return render(request, 'schedules.html')