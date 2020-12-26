from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from app1.models import Vehicle, Hotel, VehicleBookings, HotelBooking, VehicleHistory, HotelHistory


@login_required(login_url='login')
def index(request):
    return render(request, 'home.html')


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            print(user)
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')


def signupview(request):
    msg = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        try:
            User.objects.get(username=email)
            msg = 'User already exists'
        except:
            msg = None

        if password == password2:
            User.objects.create_user(username=email, first_name=name, password=password)
            msg = 'User created successfully'
        else:
            msg = 'passwords do not match'

    context = {
        'msg': msg,
    }
    return render(request, 'signup.html', context)


@login_required(login_url='login')
def logoutview(request):
    logout(request)

    return redirect('login')


def vehicleview(request):
    vehicles = Vehicle.objects.all()
    context = {
        'vehicles': vehicles
    }
    return render(request, 'vehiclebooking.html', context)


def hotelview(request):
    hotels = Hotel.objects.all()
    context = {
        'hotels': hotels
    }
    return render(request, 'hotelbooking.html', context)


def bookingsview(request):
    vehbookings = VehicleBookings.objects.filter(user=request.user)
    hotbookings = HotelBooking.objects.filter(user=request.user)

    context = {
        'vehbookings': vehbookings,
        'hotbookings': hotbookings
    }

    return render(request, 'bookinglogs.html', context)


def vbformview(request, id):
    if request.method == 'GET':

        try:
            vehicle = Vehicle.objects.get(id=id)
        except:
            return redirect('vehicle')

        context = {
            'vehicle': vehicle
        }

        return render(request, 'vbform.html', context)

    else:
        source = request.POST.get('Source')
        destination = request.POST.get('Destination')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        km = request.POST.get('kilometers')
        vehid = request.POST.get('vehid')
        total = request.POST.get('total')

        vehicle = Vehicle.objects.get(id=int(vehid))

        VehicleBookings.objects.create(
            user=request.user,
            source=source,
            destination=destination,
            from_date=startdate,
            to_date=enddate,
            kilometers=km,
            vehicle=vehicle,
            cost=total,
        )
        return redirect('logs')


def hbformview(request, id):
    if request.method == 'GET':
        try:
            hotel = Hotel.objects.get(id=id)
        except:
            return redirect('hotel')

        context = {
            'hotel': hotel
        }

        return render(request, 'hbform.html', context)

    else:
        hotel = Hotel.objects.get(id=int(request.POST.get('hotelid')))
        count=request.POST.get('noofpeople')
        ac = request.POST.get('roomtype')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        total = request.POST.get('total')

        if ac:
            ac=True
        else:
            ac=False


        HotelBooking.objects.create(
            user= request.user,
            from_date=startdate,
            to_date=enddate,
            cost=total,
            ac=ac,
            count=count,
            hotel=hotel
        )
        return redirect('logs')


@user_passes_test(lambda u: u.is_superuser)
def addvehicle(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        regno = request.POST.get('regno')
        type = request.POST.get('type')
        seats = request.POST.get('seats')
        multiplier = request.POST.get('multiplier')
        ac = request.POST.get('ac')

        if ac:
            ac=True
        else:
            ac=False

        Vehicle.objects.create(
            name=name,
            reg_no=regno,
            seats=seats,
            type=type,
            multiplier=multiplier,
            ac=ac
        )
        return redirect('vehicle')

    else:
        return render(request, 'addvehicle.html')

class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    fields = '__all__'
    template_name = 'vehicle_update.html'
    success_url = reverse_lazy('vehicle')


@user_passes_test(lambda u: u.is_superuser)
def addhotel(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('addrress')
        ac = request.POST.get('ac')
        nonac = request.POST.get('nonac')
        perperson = request.POST.get('perperson')
        noofrooms = request.POST.get('rooms')

        Hotel.objects.create(
            name=name,
            address=address,
            no_of_rooms=noofrooms,
            cost_ac=ac,
            cost_non_ac=nonac,
            cost_per_person=perperson
        )
        return redirect('hotel')

    else:
        return render(request, 'addhotel.html')

class HotelUpdateView(LoginRequiredMixin, UpdateView):
    model = Hotel
    fields = '__all__'
    template_name = 'hotel_update.html'
    success_url = reverse_lazy('hotel')


@user_passes_test(lambda u: u.is_superuser)
def deletevehicle(request, id):
    Vehicle.objects.get(id=id).delete()

    return redirect('vehicle')


@user_passes_test(lambda u: u.is_superuser)
def deletehotel(request, id):
    Hotel.objects.get(id=id).delete()

    return redirect('hotel')


@user_passes_test(lambda u: u.is_superuser)
def vehiclehistoryview(request):
    vehicles = VehicleHistory.objects.all().order_by('-created_at')
    context={
        'vehicles':vehicles
    }

    return render(request, 'vehiclehistory.html' , context)


@user_passes_test(lambda u: u.is_superuser)
def hotelhistoryview(request):
    hotels = HotelHistory.objects.all().order_by('-created_at')
    context={
        'hotels': hotels
    }

    return render(request, 'hotelhistory.html' , context)






