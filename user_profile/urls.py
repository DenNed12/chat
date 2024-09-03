from django.urls import path
from django.contrib import admin
from .views import *


app_name = 'user_profile'

urlpatterns = [
    path('profile/<int:pk>/', profile_view, name='profile'),

               ]