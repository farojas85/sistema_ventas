from django.urls import path
from .views import EmpresaView,EmpresaNew,SucursalView,SucursalNew,AlmacenView,AlmacenNew,PuntoVentaView,PuntoVentaNew

urlpatterns = [
    path('empresa/',EmpresaView.as_view(),name='empresa-inicio'),
    path('empresa/new',EmpresaNew.as_view(),name='empresa-new'),
    path('sucursal/',SucursalView.as_view(),name='sucursal-inicio'),
    path('sucursal/new',SucursalNew.as_view(),name='sucursal-new'),
    path('almacen/',AlmacenView.as_view(),name='almacen-inicio'),
    path('almacen/new',AlmacenNew.as_view(),name='almacen-new'),
    path('puntoventa/',PuntoVentaView.as_view(),name='puntoventa-inicio'),
    path('puntoventa/new',PuntoVentaNew.as_view(),name='puntoventa-new'),
]