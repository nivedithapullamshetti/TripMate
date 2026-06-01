from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# REST FRAMEWORK
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TripSerializer


# HOME PAGE
def home(request):

    return render(
        request,
        'home.html'
    )


# LOGIN + REGISTER
def accounts(request):

    if request.method == "POST":

        action = request.POST.get(
            "action"
        )

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )


        # LOGIN
        if action == "login":

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(
                    request,
                    user
                )

                return redirect(
                    'userhome'
                )

            else:

                messages.error(
                    request,
                    "Invalid Username or Password"
                )


        # REGISTER
        elif action == "register":

            if User.objects.filter(
                username=username
            ).exists():

                messages.error(
                    request,
                    "Username already exists"
                )

            else:

                User.objects.create_user(
                    username=username,
                    password=password
                )

                messages.success(
                    request,
                    "Account Created Successfully"
                )

    return render(
        request,
        'accounts.html'
    )


# USER HOME
def userhome(request):

    if not request.user.is_authenticated:

        return redirect(
            'accounts'
        )

    return render(
        request,
        'userhome.html'
    )


# LOGOUT
def logout_user(request):

    logout(
        request
    )

    return redirect(
        'home'
    )


# DASHBOARD
def dashboard(request):

    return render(
        request,
        'dashboard.html'
    )


# PLAN TRIP
def trips(request):

    if request.method == "POST":

        request.session['source'] = request.POST.get(
            'source'
        )

        request.session['destination'] = request.POST.get(
            'destination'
        )

        request.session['start_date'] = request.POST.get(
            'start_date'
        )

        request.session['end_date'] = request.POST.get(
            'end_date'
        )

        request.session['budget'] = request.POST.get(
            'budget'
        )

        request.session['transport'] = request.POST.get(
            'transport'
        )

        request.session['accommodation'] = request.POST.get(
            'accommodation'
        )

        request.session['activities'] = request.POST.get(
            'activities'
        )

        return redirect(
            'schedules'
        )

    return render(
        request,
        'trips.html'
    )


# SCHEDULE PAGE
def schedules(request):

    context = {

        'source':
        request.session.get(
            'source'
        ),

        'destination':
        request.session.get(
            'destination'
        ),

        'start_date':
        request.session.get(
            'start_date'
        ),

        'end_date':
        request.session.get(
            'end_date'
        ),

        'budget':
        request.session.get(
            'budget'
        ),

        'transport':
        request.session.get(
            'transport'
        ),

        'accommodation':
        request.session.get(
            'accommodation'
        ),

        'activities':
        request.session.get(
            'activities'
        )

    }

    return render(
        request,
        'schedules.html',
        context
    )


# SAVED TRIPS
def mytrips(request):

    context = {

        'source':
        request.session.get(
            'source'
        ),

        'destination':
        request.session.get(
            'destination'
        ),

        'budget':
        request.session.get(
            'budget'
        ),

        'transport':
        request.session.get(
            'transport'
        ),

        'accommodation':
        request.session.get(
            'accommodation'
        )

    }

    return render(
        request,
        'mytrips.html',
        context
    )


# EXPENSES
def expenses(request):

    budget = int(
        request.session.get(
            'budget',
            0
        )
    )

    transport_type = request.session.get(
        'transport'
    )

    accommodation = request.session.get(
        'accommodation'
    )


    # TRANSPORT COST

    if transport_type == "Flight":

        transport = 5000

    elif transport_type == "Train":

        transport = 2000

    elif transport_type == "Bus":

        transport = 1000

    else:

        transport = 3000


    # ACCOMMODATION COST

    if accommodation == "Hotel":

        hotel = 4000

    elif accommodation == "Resort":

        hotel = 7000

    elif accommodation == "Hostel":

        hotel = 1500

    else:

        hotel = 2000


    food = 2000
    activities = 1500


    total = (

        transport
        + hotel
        + food
        + activities

    )


    remaining = (

        budget - total

    )


    context = {

        'budget': budget,

        'transport': transport,

        'hotel': hotel,

        'food': food,

        'activities': activities,

        'total': total,

        'remaining': remaining

    }

    return render(
        request,
        'expenses.html',
        context
    )


# DESTINATIONS
def destinations(request):

    return render(
        request,
        'destinations.html'
    )


# WEATHER
def weather(request):

    return render(
        request,
        'weather.html'
    )


# REST API
@api_view(['GET'])
def trip_api(request):

    trip_data = {

        'source':
        request.session.get(
            'source'
        ),

        'destination':
        request.session.get(
            'destination'
        ),

        'start_date':
        request.session.get(
            'start_date'
        ),

        'end_date':
        request.session.get(
            'end_date'
        ),

        'budget':
        request.session.get(
            'budget'
        ),

        'transport':
        request.session.get(
            'transport'
        ),

        'accommodation':
        request.session.get(
            'accommodation'
        ),

        'activities':
        request.session.get(
            'activities'
        )

    }

    serializer = TripSerializer(
        trip_data
    )

    return Response(
        serializer.data
    )