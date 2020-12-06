from django.urls import path
from .views import MarcaView,marca_create,marca_update,marca_inhabilitar,marca_habilitar,marca_eliminar
from .views import TipoProductoView,ProductoView

urlpatterns = [
    path('marca/',MarcaView.as_view(),name="marca-inicio"),
    path('marca/crear',marca_create,name="marca-crear"),
    path('marca/<pk>/actualizar', marca_update, name='marca-actualizar'),
    path('marca/inhabilitar',marca_inhabilitar,name='marca-inhabilitar'),
    path('marca/habilitar',marca_habilitar,name="marca-habilitar"),
    path('marca/eliminar',marca_eliminar,name='marca-eliminar'),
    path('tipoproducto/',TipoProductoView.as_view(),name="tipoproducto-inicio"),
    path('producto/',ProductoView.as_view(),name='producto-inicio')
]