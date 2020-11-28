from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Departamento,Provincia,Distrito,Empresa,Sucursal,Almacen,PuntoVenta
from .forms import EmpresaForm,SucursalForm,AlmacenForm,PuntoVentaForm

# Create your views here.
class DepartamentoList(generic.View):
    def get(self, request):
        departamentos = list(Departamento.objects.all().values())
        data = dict()
        data['departamentos'] = departamentos
        return JsonResponse(data)

class ProvinciaList(generic.View):
    def get(self, request):
        provincias = list(Provincia.objects.filter(departamento_id = request.GET.get('departamento')).values('id','nombre') )
        data = dict()
        data['provincias'] = provincias
        return JsonResponse(data)

class DistritoList(generic.View):
    def get(self, request):
        distritos = list(Distrito.objects.filter(provincia_id = request.GET.get('provincia')).values('id','nombre') )
        data = dict()
        data['distritos'] = distritos
        return JsonResponse(data)

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

class EmpresaFiltro(generic.View):
    def get(self, request):
        empresa = list(Empresa.objects.filter(ruc__contains = request.GET.get('ruc')).values('id','ruc','razon_social'))
        data = dict()
        data['empresa'] = empresa
        return JsonResponse(data)

class SucursalView(LoginRequiredMixin,generic.ListView):
    paginate_by = 5
    model = Sucursal
    context_object_name = 'sucursales'
    template_name = 'emp/sucursal/inicio.html'
    login_url= 'bases:login'

class SucursalNew(LoginRequiredMixin,generic.CreateView):
    model = Sucursal,
    template_name = 'emp/sucursal/form.html'
    form_class= SucursalForm
    success_url = reverse_lazy('emp:sucursal-inicio')
    login_url = 'bases:login'

class SucursalMostrar(generic.View):
    def get(self, request):
        sucursal = list(Sucursal.objects.filter(id = request.GET.get('id')).values())
        empresa = list(Empresa.objects.filter(id = sucursal[0]['empresa_id']).values('id','ruc','razon_social'))
        ubigeo = list(Distrito.objects.filter(id = sucursal[0]['ubigeo_id']).values('id','nombre','provincia_id'))
        provincia = list(Provincia.objects.filter(id = ubigeo[0]['provincia_id']).values('id','nombre','departamento_id'))
        departamento = list(Departamento.objects.filter(id = provincia[0]['departamento_id']).values('id','nombre'))
        data = dict()
        data['sucursal'] = sucursal
        data['empresa'] = empresa
        data['ubigeo'] = ubigeo
        data['provincia'] = provincia
        data['departamento'] = departamento
        return JsonResponse(data)

class SucursalActualizar(generic.View):
    def post(self, request):
        data = dict()
        sucursal =  Sucursal.objects.get(id = request.POST['id'])
        form = SucursalForm(instance=sucursal,data= request.POST)
        if form.is_valid():
            sucursal = form.save()
            data['sucursal'] = model_to_dict(sucursal)
            data['ok'] = 1
        else:
            data['error'] = 'Formulario No Válido'
            data['ok'] = 0
        return JsonResponse(data)

class SucursalSuspender(generic.View):
    def post(self,request):
        data = dict()
        ids = request.POST.get('id_sucursal',None)
        suc =  Sucursal.objects.get(id = request.POST['id_sucursal'])
        suc.estado = 0
        suc.save()
        data['sucursal'] = model_to_dict(suc)
        data['ok'] = 1
        return JsonResponse(data)

class AlmacenView(LoginRequiredMixin,generic.ListView):
    paginate_by = 5
    model = Almacen
    context_object_name = 'almacenes'
    template_name = 'emp/almacen/inicio.html'
    login_url= 'bases:login'

class AlmacenNew(LoginRequiredMixin,generic.CreateView):
    model = Almacen,
    template_name = 'emp/almacen/form.html'
    form_class= AlmacenForm
    success_url = reverse_lazy('emp:almacen-inicio')
    login_url = 'bases:login'

class PuntoVentaView(LoginRequiredMixin,generic.ListView):
    paginate_by = 5
    model = PuntoVenta
    context_object_name = 'puntoventas'
    template_name = 'emp/puntoventa/inicio.html'
    login_url= 'bases:login'

class PuntoVentaNew(LoginRequiredMixin,generic.CreateView):
    model = PuntoVenta,
    template_name = 'emp/puntoventa/form.html'
    form_class= PuntoVentaForm
    success_url = reverse_lazy('emp:puntoventa-inicio')
    login_url = 'bases:login'