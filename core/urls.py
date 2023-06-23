from django.urls import path
from .views import contactos, eventos, home, info, ingreso, registro, tienda, login

urlpatterns = [
    path('', home, name="home"),
    path('contactos/', contactos, name="contactos"),
    path('eventos/', eventos, name="eventos"),
    path('info/', info, name="info"),
    path('ingreso/', ingreso, name="ingreso"),
    path('registro/', registro, name="registro"),
    path('tienda/', tienda, name="tienda"),
    path('login/', login, name="login" )
]