from django.contrib import admin
#yo
from .models import *
# Register your models here.
#yo

class SucursalAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)

class GeneroAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)

class EventosAdmin(admin.ModelAdmin):
    list_display = ('id', "nombreEvento", "fechaInicio", "fechaFin")
    search_fields = ("nombreEvento",)

admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Evento, EventosAdmin)
