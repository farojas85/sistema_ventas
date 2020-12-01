from django.urls import path
from .views import MarcaView,TipoProductoView,ProductoView

urlpatterns = [
    path('marca/',MarcaView.as_view(),name="marca-inicio"),
    path('tipoproducto/',TipoProductoView.as_view(),name="tipoproducto-inicio"),
    path('producto/',ProductoView.as_view(),name='producto-inicio')
]