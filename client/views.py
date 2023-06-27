from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from .services.user_service import UserService
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.

user_service = UserService()

@login_required
def chat(request):

    # Obtén los datos necesarios del backend
    context = {'message': 'Hola desde el backend'}

    return render(request, 'chat.html', context)

@login_required
def lobby(request):
    return render(request, 'lobby.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('lobby')  # Redirige a la página de inicio después del inicio de sesión exitoso
        else:
            error_message = 'Username or password not correct'
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        phone = request.POST['phone']
        # Use the service to create the user
        user_service.add(username, email, password, address, phone)
        return redirect('login')
    return render(request, 'register.html')