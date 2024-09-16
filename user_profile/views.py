from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView


@login_required
def profile_view(request, pk):

    profile = Profile.objects.get(user= request.user)

    return render(request, 'user_profile.html', {'profile': profile})


def profile_edit(request,pk):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'user_profile.html', context)


class ProfileEdit(UpdateView):
    template_name = 'profile_edit.html'
    model = Profile
    form_class = ProfileUpdateForm



class UserDetail(DetailView):
    model = Profile
    context_object_name = 'profile'


class GetUserList(ListView):
    model = Profile
    template_name = 'user_list.html'
    paginate_by = 5
    context_object_name = 'profiles'
    print('Oh hi')
