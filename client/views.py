from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from .services.user_service import UserService
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

# Create your views here.

user_service = UserService()

# @login_required
def home(request):
    return render(request, 'home.html')

# @login_required
def lobby(request):
    return render(request, 'lobby.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print("Esto es email: ", email)
        password = request.POST.get('password')
        print("Esto es password: ", password)
        user = authenticate(request, email=email, password=password)
        print("Esto es user: ", user)
        
        if user is not None:
            login(request, user)
            return redirect('lobby')  # Redirige a la página de inicio después del inicio de sesión exitoso
        else:
            error_message = 'Email or password not correct'
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        account_id = request.POST.get('account_id')
        print("Esto es account id: ", account_id)

        # Hash the password
        hashed_password = make_password(password)

        # Use the service to create the user
        user_service.add(username, email, hashed_password, address, phone, account_id)
        return redirect('login')
    return render(request, 'register.html')