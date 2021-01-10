from django.db import models
from bases.models import ClaseModelo
from emp.models import Empresa,Almacen,UnidadMedida,Sucursal

class TipoComprobante(models.Model):
	id = models.BigAutoField(primary_key=True,verbose_name='ID')
	codigo = models.CharField(max_length=2,help_text="Código de Comprobante",blank=True, null=True)
	nombre = models.CharField(max_length=191,help_text="Nombre Tipo Comprobante",blank=True, null=True)
	estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

class Serie(models.Model):
	id = models.BigAutoField(primary_key=True,verbose_name='ID')
	sucursal = models.ForeignKey(Sucursal,on_delete=models.CASCADE,blank=True, null=True)
	codigo = models.CharField(max_length=3,help_text="Código Forma de Pago",blank=True, null=True)
	nombre = models.CharField(max_length=191,help_text="Nombre Forma de Pago",blank=True, null=True)
	estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

class FormaPago(models.Model):
	id = models.BigAutoField(primary_key=True,verbose_name='ID')
	codigo = models.CharField(max_length=3,help_text="Código Forma de Pago",blank=True, null=True)
	nombre = models.CharField(max_length=191,help_text="Nombre Forma de Pago",blank=True, null=True)
	estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

class ComprobanteVenta(models.Model):
	id = models.BigAutoField(primary_key=True,verbose_name='ID')
	sucursal = models.ForeignKey(Sucursal,on_delete=models.CASCADE,blank=True, null=True)
	tipo_comprobante = models.ForeignKey(TipoComprobante,on_delete=models.CASCADE,blank=True, null=True)
