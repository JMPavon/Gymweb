from django.db import models

# Create your models here.
#yo
class CompaniaInfo(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    urlLogo = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural='CompaniasInfo'

    def __str__(self):
        return self.nombre


class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    company = models.ForeignKey(CompaniaInfo, on_delete=models.CASCADE)


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


class Evento(models.Model):
    nombreEvento = models.CharField(max_length=100, verbose_name='Evento')
    fechaInicio = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Inicio')
    fechaFin = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Fin')

    class meta:
        verbose_name_plural='Eventos'
        verbose_name="Evento"

    def __str__(self):
        return self.nombreEvento


class Cliente(models.Model):
    dni = models.CharField(max_length=13, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
