from django.urls import path
from .views import MarcaView,marca_create,marca_update,marca_inhabilitar,marca_habilitar,marca_eliminar
from .views import CategoriaView,categoria_create,categoria_update,categoria_inhabilitar,categoria_habilitar,categoria_eliminar
from .views import TipoProductoView
from .views import ProductoView,ProductoCreate
from .views import EmpresaList

urlpatterns = [
    path('marca/',MarcaView.as_view(),name="marca-inicio"),
    path('marca/crear',marca_create,name="marca-crear"),
    path('marca/<pk>/actualizar', marca_update, name='marca-actualizar'),
    path('marca/inhabilitar',marca_inhabilitar,name='marca-inhabilitar'),
    path('marca/habilitar',marca_habilitar,name="marca-habilitar"),
    path('marca/eliminar',marca_eliminar,name='marca-eliminar'),
    path('categoria/',CategoriaView.as_view(),name="categoria-inicio"),
    path('categoria/crear',categoria_create,name="categoria-crear"),
    path('categoria/<pk>/actualizar',categoria_update,name="categoria-actualizar"),
    path('categoria/inhabilitar',categoria_inhabilitar,name="categoria-inhabilitar"),
    path('categoria/habilitar',categoria_habilitar,name="categoria-habilitar"),
    path('categoria/eliminar',categoria_eliminar,name="categoria-eliminar"),
    path('tipoproducto/',TipoProductoView.as_view(),name="tipoproducto-inicio"),
    path('empresa/lista',EmpresaList.as_view(),name="empresa-lista"),
    path('producto/',ProductoView.as_view(),name='producto-inicio'),
    path('producto/crear',ProductoCreate.as_view(),name="producto-crear")
]