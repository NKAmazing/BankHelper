from django.shortcuts import render

# Create your views here.

def chat(request):

    # Obtén los datos necesarios del backend
    context = {'message': 'Hola desde el backend'}

    return render(request, 'chat.html', context)
