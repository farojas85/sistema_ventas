from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.forms.models import model_to_dict
from django.db.models import Q,Count,FilteredRelation
from .models import ComprobanteVenta
from .forms import ComprobanteVentaForm

class ComprobanteVentaView(LoginRequiredMixin,generic.CreateView):
    model = ComprobanteVenta
    context_object_name = 'comprobante_ventas'
    template_name = 'ventas/boleta-factura/inicio.html'
    form_class= ComprobanteVentaForm
    login_url= 'bases:login'
