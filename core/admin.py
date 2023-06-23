from django.contrib import admin
from .models import *

# Register your models here.

class IngresoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'contraseña']
    search_fields = ['nombre', 'email']
    list_filter = ['nombre']
    list_per_page = 10

class ConciertoAdmin(admin.ModelAdmin):
    list_display = ['lugar','personas_total', 'fecha']
    search_fields = ['lugar', 'fecha']
    list_filter = ['lugar']
    list_per_page = 10

class EntradaAdmin(admin.ModelAdmin):
    list_display = ['tipo_entrada','conciert','stock','precio']
    search_fields = ['conciert']
    list_filter = ['conciert']
    list_per_page = 10

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente','Concierto','entrada','cantidad','total']
    search_fields = ['entrada']
    list_filter = ['entrada']
    list_per_page = 10

admin.site.register(Ingreso, IngresoAdmin)
admin.site.register(Concierto,ConciertoAdmin)
admin.site.register(Entrada,EntradaAdmin)
admin.site.register(Pedido,PedidoAdmin)