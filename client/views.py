from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services.user_service import UserService
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from server.functions import search_user
import json

# Create your views here.

user_service = UserService()

def home(request):
    return render(request, 'home.html')

@login_required(login_url='/client/login/')
def lobby(request):
    return render(request, 'lobby.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        result = search_user(request, email)
        print("ESTO ES DATA: ", result)
        if result:            
            # Get the password
            passw = result['password']

            print("ESTO ES PASSW: ", passw)

            # Check if the password is correct
            if password == passw:
                # Set the session cookie
                session_key = request.session.session_key
                expiry_date = datetime.now() + timedelta(hours=1)
                response = HttpResponseRedirect('/lobby/')
                response.set_cookie('sessionid', session_key, expires=expiry_date)
                return response
            else:
                return HttpResponse('Password incorrect')
        else:
            return HttpResponse('User not found')
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

def logout_view(request):
    # Eliminar la cookie de sesión
    response = HttpResponseRedirect('/login/')
    response.delete_cookie('sessionid')

    # Limpiar la sesión actual
    request.session.flush()

    # Redireccionar al usuario a la página de inicio de sesión
    return response
