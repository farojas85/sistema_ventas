from django.urls import path
from .views import EmpresaView,EmpresaNew

urlpatterns = [
    path('empresa/',EmpresaView.as_view(),name='empresa-inicio'),
    path('empresa/new',EmpresaNew.as_view(),name='empresa-new')
]