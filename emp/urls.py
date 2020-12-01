from django.urls import path
from .views import DepartamentoList, ProvinciaList,DistritoList,EmpresaView,EmpresaNew,EmpresaFiltro
from .views import SucursalView,SucursalNew,SucursalMostrar,SucursalActualizar,SucursalSuspender
from .views import SucursalBuscar,SucursalPorId
from .views import TipoAlmacenLista,UnidadMedidaLista
from .views import AlmacenView,AlmacenNew,AlmacenMostrar,AlmacenActualizar
from .views import PuntoVentaView,PuntoVentaNew

urlpatterns = [
    path('departamento/list', DepartamentoList.as_view(), name='departamento_list'),
    path('provincia/list_by_departamento',ProvinciaList.as_view(), name="provincia_list"),
    path('distrito/list_by_provincia',DistritoList.as_view(), name="distrito_list"),
    path('empresa/',EmpresaView.as_view(),name='empresa-inicio'),
    path('empresa/new',EmpresaNew.as_view(),name='empresa-new'),
    path('empresa/filtro',EmpresaFiltro.as_view(),name='empresa_filtro'),
    path('sucursal/',SucursalView.as_view(),name='sucursal-inicio'),
    path('sucursal/new',SucursalNew.as_view(),name='sucursal-new'),
    path('sucursal/mostrar',SucursalMostrar.as_view(),name='sucursal-mostrar'),
    path('sucursal/actualizar',SucursalActualizar.as_view(),name='sucursal-actualizar'),
    path('sucursal/eliminar',SucursalSuspender.as_view(),name='sucursal-eliminar'),
    path('sucursal/buscar',SucursalBuscar.as_view(),name="sucursal-buscar"),
    path('sucursal/por-id',SucursalPorId.as_view(),name="sucursal-por-id"),
    path('tipo-almacen/lista',TipoAlmacenLista.as_view(),name="tipo-almacen-lista"),
    path('unidad-medida/lista',UnidadMedidaLista.as_view(),name="unidad-medida-lista"),
    path('almacen/',AlmacenView.as_view(),name='almacen-inicio'),
    path('almacen/new',AlmacenNew.as_view(),name='almacen-new'),
    path('almacen/mostrar',AlmacenMostrar.as_view(),name="almacen-mostrar"),
    path('almacen/actualizar',AlmacenActualizar.as_view(),name="almacen-actualizar"),
    path('puntoventa/',PuntoVentaView.as_view(),name='puntoventa-inicio'),
    path('puntoventa/new',PuntoVentaNew.as_view(),name='puntoventa-new'),
]