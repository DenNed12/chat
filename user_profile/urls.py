from django.urls import path
from django.contrib import admin
from .views import *


app_name = 'user_profile'

urlpatterns = [
    path('profile/<int:pk>/', profile_view, name='profile'),
    path('profile/<int:pk>/edit/', ProfileEdit.as_view(), name='profile_edit'),
    path('user_list/', GetUserList.as_view(), name = 'user_list')

    ]