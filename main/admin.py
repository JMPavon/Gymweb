from django.contrib import admin
#yo
from .models import *
# Register your models here.
#yo

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)

#admin.site.register(Sucursal, SucursalAdmin)

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)

@admin.register(Evento)
class EventosAdmin(admin.ModelAdmin):
    list_display = ('id', "nombreEvento", "fechaInicio", "fechaFin")
    search_fields = ("nombreEvento",)




