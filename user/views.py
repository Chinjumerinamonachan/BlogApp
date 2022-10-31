from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.views import generic as views
from django.conf import settings
from django.contrib.auth import get_user_model
from user.forms import UserLoginForm, CustomUserRegistrationForm
from django.contrib.auth import authenticate,login

USER = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password,email=user.email)

           
            return redirect('myblog:home')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_page(request):
    form = form.UserLoginForm()
    # message = ''
    if request.method == 'POST':
        form = form.UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )

        if user is not None:
                login(request, user)
           
        else:
            form = UserLoginForm()
            
    return render(request, 'registration/login.html', context={'form': form})





    

