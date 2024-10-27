# rentals/forms.py
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class CustomUserRegistrationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('Seller', 'Seller'),
        ('Client', 'Client')
    ]
    
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label="Register as")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
