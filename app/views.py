# rentals/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import CustomUserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            role = form.cleaned_data['role']
            user.save()

            # Assign the user to the correct group
            if role == 'Seller':
                seller_group = Group.objects.get(name='Seller')
                user.groups.add(seller_group)
            elif role == 'Client':
                client_group = Group.objects.get(name='Client')
                user.groups.add(client_group)

            # Log in the user and redirect based on role
            login(request, user)
            if role == 'Seller':
                return redirect('seller_dashboard')
            else:
                return redirect('client_dashboard')
    else:
        form = CustomUserRegistrationForm()  # Initialize form for GET request

    return render(request, 'register.html', {'form': form})
