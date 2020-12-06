from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.forms.models import model_to_dict
from django.db.models import Q
from emp.models import Empresa
from .models import Marca,TipoProducto,Producto,Categoria
from .forms import MarcaForm,CategoriaForm,ProductoForm

class MarcaView(LoginRequiredMixin,generic.ListView):
    model = Marca
    context_object_name = 'marcas'
    template_name = 'prod/marca/inicio.html'
    login_url= 'bases:login'


def marca_create(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
    else:
        form = MarcaForm()
    return marca_form_save(request,form)

def marca_form_save(request,form):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    context = {'form': form}    
    data['html_form']= render_to_string('prod/marca/form.html',context,request=request)
    return JsonResponse(data)

def marca_update(request,pk):
    marca = get_object_or_404(Marca,pk=pk)
    if(request.method=='POST'):
        form = MarcaForm(request.POST,instance = marca)
    else:
        form = MarcaForm(instance=marca)
    return marca_form_save(request,form)

def marca_inhabilitar(request):
    data = dict()
    marca =  Marca.objects.get(id =request.POST['id_marca'])
    marca.estado = 0
    marca.save()
    data['marca'] = model_to_dict(marca)
    data['ok'] = 1
    return JsonResponse(data)

def marca_habilitar(request):
    data = dict()
    marca =  Marca.objects.get(id =request.POST['id_marca_habilitar'])
    marca.estado = 1
    marca.save()
    data['marca'] = model_to_dict(marca)
    data['ok'] = 1
    return JsonResponse(data)

def marca_eliminar(request):
    data = dict()
    producto_count = Producto.objects.filter(marca_id=request.POST['id_marca']).exists()
    marca =  Marca.objects.get(id =request.POST['id_marca'])

    if(producto_count):
        data['ok'] = 0
        data['mensaje'] = 'La marca ya contiene Productos'
    else:
        marca.delete()
        data['ok'] = 1
        data['mensaje'] ='Marca Eliminada Satisfactoriamente'
        data['marca'] = model_to_dict(marca)
    
    return JsonResponse(data)

class CategoriaView(LoginRequiredMixin,generic.ListView):
    model = Categoria
    context_object_name = 'categorias'
    template_name='prod/categoria/inicio.html'
    login_url= 'bases:login'

def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
    else:
        form = CategoriaForm()
    return categoria_form_save(request,form)

def categoria_form_save(request, form):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    context = {'form': form}    
    data['html_form']= render_to_string('prod/categoria/form.html',context,request=request)
    return JsonResponse(data)

def categoria_update(request,pk):
    categoria = get_object_or_404(Categoria,pk=pk)
    if(request.method=='POST'):
        form = CategoriaForm(request.POST,instance = categoria)
    else:
        form = CategoriaForm(instance=categoria)
    return categoria_form_save(request,form)

def categoria_inhabilitar(request):
    data = dict()
    categoria =  Categoria.objects.get(id =request.POST['id_categoria'])
    categoria.estado = 0
    categoria.save()
    data['categoria'] = model_to_dict(categoria)
    data['ok'] = 1
    return JsonResponse(data)

def categoria_habilitar(request):
    data = dict()
    categoria =  Categoria.objects.get(id =request.POST['id_categoria_habilitar'])
    categoria.estado = 1
    categoria.save()
    data['categoria'] = model_to_dict(categoria)
    data['ok'] = 1
    return JsonResponse(data)

def categoria_eliminar(request):
    data = dict()
    producto_count = Producto.objects.filter(categoria_id=request.POST['id_categoria']).exists()
    categoria =  Categoria.objects.get(id =request.POST['id_categoria'])

    if(producto_count):
        data['ok'] = 0
        data['mensaje'] = 'La categoría ya contiene Productos'
    else:
        categoria.delete()
        data['ok'] = 1
        data['mensaje'] ='Categoría Eliminada Satisfactoriamente'
        data['categoria'] = model_to_dict(categoria)
    
    return JsonResponse(data)

class TipoProductoView(LoginRequiredMixin,generic.ListView):
    model = TipoProducto
    context_object_name = 'tipoproductos'
    template_name = 'prod/tipoproducto/inicio.html'
    login_url= 'bases:login'

class ProductoView(LoginRequiredMixin,generic.ListView):
    model = Producto
    context_object_name ='productos'
    template_name = 'prod/producto/inicio.html'
    login_url = 'bases:login'

class EmpresaList(generic.View):
    def get(self, request):
        data = dict()
        data['empresas'] = list(Empresa.objects.all().values('id','razon_social'))
        return JsonResponse(data)

class CategoriaLista(generic.View):
    def get(self,request):
        data = dict()

class ProductoCreate(LoginRequiredMixin,generic.CreateView):
    model = Producto
    template_name = 'prod/producto/form.html'
    form_class= ProductoForm
    success_url = reverse_lazy('prod:producto-inicio')
    login_url = 'bases:login'
