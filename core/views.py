from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'core/home.html')

def contactos(request):
    return render(request, 'core/contactos.html')

def eventos(request):
    return render(request, 'core/eventos.html')

def ingreso(request):
    return render(request, 'core/ingreso.html')

def registro(request):
    return render(request, 'core/registro.html')

def info(request):
    return render(request, 'core/info.html')

@login_required
def tienda(request):
    return render(request, 'core/tienda.html')

def login(request):
    return render(request, 'core/login.html')