from dataclasses import fields
from enum import unique
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# from user.models import UserProfile

USER = get_user_model()


class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200,help_text='Required') 
    class Meta:
        model = USER
        fields = ["username", "password1", "password2","email","first_name","last_name","date_of_birth","Phone_no"]




class UserLoginForm(forms.Form):
    username = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())

