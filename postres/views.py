from django.shortcuts import render

# Create your views here.


from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Postres

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms


class PostresListado(ListView): 
    model = Postres 


class PostreCrear(SuccessMessageMixin, CreateView):
    model = Postres
    form = Postres
    fields = "__all__"
    seccess_message = 'Postre Creado Correctamente !'

    def get_success_url(self):
        return reverse('leer')



class PostreDetalle(DetailView):
    model = Postres



class PostreActualizar(SuccessMessageMixin, UpdateView):
    model = Postres
    form = Postres 
    fields = "__all__"
    success_message = 'Postre Actualizado correctamente !'

    def get_success_url(self):
        return reverse('leer')

class PostreEliminar(SuccessMessageMixin, DeleteView):
    model = Postres 
    form = Postres
    fields = "__all__"

    def get_success_url(self):
        seccess_message ='Postre Eliminados Correctamente !'
        messages.success (self.request,(seccess_message))
        return reverse('leer')        


