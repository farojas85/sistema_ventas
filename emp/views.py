from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Empresa
from .forms import EmpresaForm
# Create your views here.
class EmpresaView(LoginRequiredMixin,generic.ListView):
    paginate_by = 5
    model = Empresa
    context_object_name = 'empresas'
    template_name = 'emp/empresa/inicio.html'
    login_url= 'bases:login'

class EmpresaNew(LoginRequiredMixin,generic.CreateView):
    model = Empresa,
    template_name = 'emp/empresa/form.html'
    form_class= EmpresaForm
    success_url = reverse_lazy('emp:empresa-inicio')
    login_url = 'bases:login'

    # def form_valid(self,form):
    #     form.instance.