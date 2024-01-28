from django.shortcuts import render
from .forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


# Create your views here.
def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])

            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('basic_page'))
            else:
                messages.info(request, "Something wrong with your Login or Password")
    else:
        form = LoginUserForm()
    return render(request, 'userlogin/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
