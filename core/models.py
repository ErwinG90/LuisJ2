from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import RegexValidator, MinLengthValidator, MinValueValidator, MaxLengthValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

    
class Concierto(models.Model):
    id = models.AutoField(primary_key=True)
    lugar = models.CharField(max_length=100,null=False)
    personas_total = models.IntegerField(null=False,validators=[MinValueValidator(0)])
    fecha = models.DateTimeField(null=False)

    def __str__(self):
        return self.lugar
    
class Entrada(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_entrada = models.CharField(null=False,max_length=200)
    conciert = models.ForeignKey(Concierto,null=False, on_delete=CASCADE)
    stock = models.IntegerField(null=False,validators=[MinValueValidator(0)])
    precio = models.IntegerField(null=False,validators=[MinValueValidator(0)])

    def __str__(self):
        return self.tipo_entrada

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(User,null=False, on_delete=CASCADE)
    Concierto = models.ForeignKey(Concierto,null=False, on_delete=CASCADE)
    entrada = models.ForeignKey(Entrada,null=False, on_delete=CASCADE)
    cantidad = models.IntegerField(null=False,validators=[MinValueValidator(0)])
    objeto_p = Entrada.objects.first()
    precio = Entrada.objects.get(pk=objeto_p.pk).precio
    
    def total(self):
            resultado = self.precio * self.cantidad
            return resultado

    def __str__(self):
        return f'Pedido: {self.cliente}'
