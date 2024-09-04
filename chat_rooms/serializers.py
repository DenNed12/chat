from rest_framework import serializers
from .models import Message,Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('name','slug')




class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['room', 'content','user','date_added']


