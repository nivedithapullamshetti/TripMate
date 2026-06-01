from django.shortcuts import render

def expenses_home(request):
    return render(request, 'expenses.html')