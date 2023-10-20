from django.contrib import admin
#yo
from .models import *
# Register your models here.
#yo

class SucursalAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "email")
    search_fields = ("nombre",)

admin.site.register(Sucursal, SucursalAdmin)
