"""
URL configuration for gymweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('clientes/', ListaClientes.as_view(), name="clientes"),
    path('clientes/agregar/', CrearCliente.as_view(), name="crear_cliente"),
    path('clientes/editar/<slug:pk>/', EditarCliente.as_view(), name="editar_cliente"),
    path('clientes/eliminar/<slug:pk>/', EliminarCliente.as_view(), name="eliminar_cliente"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
