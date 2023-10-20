from django.db import models

# Create your models here.
#yo
class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        verbose_name_plural='Sucursales'

    def __str__(self):
        return self.nombre


class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    class meta:
        verbose_name_plural='Generos'

    def __str__(self):
        return self.nombre