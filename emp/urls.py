from django.urls import path
from .views import DepartamentoList, ProvinciaList,DistritoList,EmpresaView,EmpresaNew,SucursalView,SucursalNew,AlmacenView,AlmacenNew,PuntoVentaView,PuntoVentaNew

urlpatterns = [
    path('departamento/list', DepartamentoList.as_view(), name='departamento_list'),
    path('provincia/list_by_departamento',ProvinciaList.as_view(), name="provincia_list"),
    path('distrito/list_by_provincia',DistritoList.as_view(), name="distrito_list"),
    path('empresa/',EmpresaView.as_view(),name='empresa-inicio'),
    path('empresa/new',EmpresaNew.as_view(),name='empresa-new'),
    #path('empresa/departamento/lista')
    path('sucursal/',SucursalView.as_view(),name='sucursal-inicio'),
    path('sucursal/new',SucursalNew.as_view(),name='sucursal-new'),
    path('almacen/',AlmacenView.as_view(),name='almacen-inicio'),
    path('almacen/new',AlmacenNew.as_view(),name='almacen-new'),
    path('puntoventa/',PuntoVentaView.as_view(),name='puntoventa-inicio'),
    path('puntoventa/new',PuntoVentaNew.as_view(),name='puntoventa-new'),
]