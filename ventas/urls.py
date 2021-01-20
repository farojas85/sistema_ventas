from django.urls import path
from .views import ComprobanteVentaView

urlpatterns = [
    path('boleta-factura/',ComprobanteVentaView.as_view(),name="boleta-factura-inicio")
]