from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('contactos/', contactos, name="contactos"),
    path('eventos/', eventos, name="eventos"),
    path('info/', info, name="info"),
    path('registro/', register, name='registro'),
    path('tienda/', tienda, name="tienda"),
    path('login/', login, name="login"),


    path('Gestion/', Gestion, name="Gestion"),

    path('ModificarConcierto/<id>/', ModificarConcierto, name="ModificarConcierto"),
    path('ModificarEntrada/<id>/', ModificarEntrada, name="ModificarEntrada"),
    path('ModificarCliente/<username>/', ModificarCliente, name="ModificarCliente"),
    path('ModificarPedido/<id>/', ModificarPedido, name="ModificarPedido"),


    path('Agregar_Concierto/', CrearConcierto, name="CrearConcierto"),
    path('Agregar_Entrada/', CrearEntrada, name="CrearEntrada"),
    path('Agregar_Cliente/', CrearCliente, name="CrearCliente"),
    path('Agregar_Pedido/', CrearPedido, name="CrearPedido"),

    path('EliminarConcierto/<id>/', EliminarConcierto, name="EliminarC"),
    path('EliminarEntrada/<id>/', EliminarEntrada, name="EliminarE"),
    path('EliminarCliente/<email>/', EliminarCliente, name="EliminarCli"),
    path('EliminarPedido/<id>/', EliminarPedido, name="EliminarP"),
]