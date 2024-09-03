from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
@login_required
def profile_view(request, pk):
    print('lol_kek')
    profile = Profile.objects.get(user= request.user)
    print('oh_lol')
    return render(request, 'user_profile.html', {'profile': profile})
