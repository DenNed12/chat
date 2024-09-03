from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignupForm
# Create your views here.
def frontpage(request):
    return render(request,'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print('Hello there')
        if form.is_valid():
            print('Form is valid')
            user = form.save()
            login(request, user)
            return redirect('core:frontpage')
        else:
            print('Form is not valid:', form.errors)
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})



