from django.shortcuts import render
from .models import Room
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request,'rooms/room.html', {'rooms':rooms} )



@login_required
def room(request, room_name):

    return render(request, 'rooms/single_room.html', {'room_name': room_name})
