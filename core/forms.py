from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    pass
    


class ConciertoForm(forms.ModelForm):

    class Meta:
        model = Concierto
        fields = "__all__"

class EntradaForm(forms.ModelForm):

    class Meta:
        model = Entrada
        fields = "__all__"

class ClienteForm(forms.ModelForm):

    class Meta:
        model = User
        fields = "__all__"

class PedidoTiendaForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PedidoTiendaForm, self).__init__(*args, **kwargs)
        
        if user is not None:
            self.initial['cliente'] = user
            self.fields['cliente'].disabled = True

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = "__all__"