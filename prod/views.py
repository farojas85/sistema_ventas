from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.db.models import Q
from .models import Marca,TipoProducto,Producto

class MarcaView(LoginRequiredMixin,generic.ListView):
    paginate_by = 5
    model = Marca
    context_object_name = 'marcas'
    template_name = 'prod/marca/inicio.html'
    login_url= 'bases:login'

class TipoProductoView(LoginRequiredMixin,generic.ListView):
    paginate_by = 5
    model = TipoProducto
    context_object_name = 'tipoproductos'
    template_name = 'prod/tipoproducto/inicio.html'
    login_url= 'bases:login'

class ProductoView(LoginRequiredMixin,generic.ListView):
    paginate_by = 5
    model = Producto
    context_object_name ='productos'
    template_name = 'prod/producto/inicio.html'
    login_url = 'bases:login'