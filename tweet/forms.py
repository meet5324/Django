from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('text', 'photo')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User  # Fix: Define model
        fields = ('username', 'email', 'password1', 'password2')
