from django.urls import path
from . import views

app_name = 'chat_rooms'

urlpatterns = [
    path('', views.rooms, name='chat-rooms'),
    path('<str:room_name>/', views.room, name='single_room'),

]
