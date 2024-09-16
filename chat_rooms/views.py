from django.shortcuts import render
from .models import Room
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Room, Message,User
from .serializers import RoomSerializer, MessageSerializer
from django.views.generic import ListView, DetailView
# Create your views here.

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request,'rooms/room.html', {'rooms':rooms} )



@login_required
def room(request, room_name):

    return render(request, 'rooms/single_room.html', {'room_name': room_name})




class GetRoomInfoView(APIView):
    def get(self, request):

        queryset = Room.objects.all()
        serializer_for_queryset = RoomSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)



