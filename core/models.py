from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Ingreso(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=80)
    contraseña = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre
    
class Concierto(models.Model):
    lugar = models.CharField(max_length=100)
    personas_total = models.IntegerField()
    fecha = models.DateTimeField()

    def __str__(self):
        return self.lugar
    
class Entrada(models.Model):
    tipo_entrada = models.CharField(max_length=200)
    conciert = models.ForeignKey(Concierto, on_delete=CASCADE)
    stock = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return self.tipo_entrada

class Pedido(models.Model):
    cliente = models.ForeignKey(Ingreso, on_delete=CASCADE)
    Concierto = models.ForeignKey(Concierto, on_delete=CASCADE)
    entrada = models.ForeignKey(Entrada, on_delete=CASCADE)
    cantidad = models.IntegerField()
    objeto_p = Entrada.objects.first()
    precio = Entrada.objects.get(pk=objeto_p.pk).precio
    
    def total(self):
            resultado = self.precio * self.cantidad
            return resultado

    def __str__(self):
        return f'Pedido: {self.cliente}'
