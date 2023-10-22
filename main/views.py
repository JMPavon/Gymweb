from django.shortcuts import render
from datetime import datetime
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    ctx = {
        "variable": datetime.now()
    }
    return render(request, "home.html", ctx)


# def clientes(request):
#     ctx = {
#         "lista": Cliente.objects.all()
#     }
#     return render(request, "clientes.html", ctx)


# def crearCliente(request):
#     if request.method == "POST":
#         form = FrmCliente(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#             except:
#                 pass
#             else:
#                 return HttpResponseRedirect(reverse('clientes'))
#     else:
#         form = FrmCliente()
#     ctx = {
#         "form": form
#     }
#     return render(request, "crear_cliente.html", ctx)


class ListaClientes(ListView):
    model = Cliente
    template_name = "clientes.html"
    context_object_name = "lista"


# class CrearCliente(CreateView):
#     model = Cliente
#     form_class = FrmCliente
#     template_name = "crear_cliente.html"
#
#     def get_success_url(self):
#         return reverse('clientes')
#
#     def get_context_data(self):
#         ctx = super(CrearCliente, self).get_context_data()
#         ctx["titulo"] = "Crear"
#         return ctx
#
#
# class EditarCliente(UpdateView):
#     model = Cliente
#     form_class = FrmCliente
#     template_name = "crear_cliente.html"
#
#     def get_success_url(self):
#         return reverse('clientes')
#
#     def get_context_data(self, **kwargs):
#         ctx = super(EditarCliente, self).get_context_data()
#         ctx["titulo"] = "Editar"
#         return ctx


class Padre(View):
    model = Cliente
    form_class = FrmCliente
    template_name = "crear_cliente.html"
    titulo = None

    def get_success_url(self):
        return reverse('clientes')

    def get_context_data(self, **kwargs):
        ctx = super(Padre, self).get_context_data()
        ctx["titulo"] = self.titulo
        return ctx


class CrearCliente(Padre, CreateView):
    titulo = "Crear"


class EditarCliente(Padre, UpdateView):
    titulo = "Editar"


class EliminarCliente(DeleteView):
    model = Cliente
    template_name = "eliminar_cliente.html"
    success_url = reverse_lazy('clientes')

    # def delete(self, request, *args, **kwargs):
    #     """
    #     Call the delete() method on the fetched object and then redirect to the
    #     success URL.
    #     """
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     # self.object.delete()
    #     return HttpResponseRedirect(success_url)
