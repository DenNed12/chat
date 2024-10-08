from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer
import json
from asgiref.sync import async_to_sync,sync_to_async
from django.contrib.auth.models import User
from .models import Room, Message
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )


    async def receive(self, text_data):
        print(text_data)
        data = json.loads(text_data)
        print("Data", data)
        message = data['message']
        username = data['username']

        await self.channel_layer.group_send (
            self.room_group_name, {"type": "chat_message", "message": message,'username':username}
        )


    async def chat_message(self, event):
        print(event)
        message = event['message']
        username =event['username']


        await self.send(text_data=json.dumps({"message": message}))


    async def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)

        await Message.objects.create(user=user, room=room, content=message)

#