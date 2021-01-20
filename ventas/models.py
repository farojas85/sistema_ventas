from django.db import models
from bases.models import ClaseModelo
from emp.models import Empresa,Almacen,UnidadMedida,Sucursal
from prod.models import Producto,UnidadMedida

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

class Moneda(models.Model):
	id = models.BigAutoField(primary_key=True,verbose_name='ID')
	codigo = models.CharField(max_length=3,help_text="Código Forma de Pago",blank=True, null=True)
	nombre = models.CharField(max_length=191,help_text="Nombre Forma de Pago",blank=True, null=True)
	estado = models.BooleanField(default=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)

class EstadoOperacion(models.Model):
	id = models.BigAutoField(primary_key=True,verbose_name='ID')
	nombre = models.CharField(max_length=191,help_text="Nombre Estado Operación",blank=True, null=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)

class ComprobanteVenta(models.Model):
	id = models.BigAutoField(primary_key=True,verbose_name='ID')
	sucursal = models.ForeignKey(Sucursal,on_delete=models.CASCADE,blank=True, null=True)
	tipo_comprobante = models.ForeignKey(TipoComprobante,on_delete=models.CASCADE,blank=True, null=True)
	serie_comprobante = models.CharField(max_length=4,help_text="Serie Comprobante")
	numero_comprobante = models.PositiveIntegerField(help_text="Número Comprobante")
	fecha = models.DateTimeField(help_text="Fecha Comprobante")
	sub_total = models.DecimalField(max_digits=18,decimal_places=2,help_text="Sub Total")
	igv = models.DecimalField(max_digits=18,decimal_places=2,help_text="Sub Total",default=0.00)
	descuento = models.DecimalField(max_digits=18,decimal_places=2,help_text="Descuento",default=0.00)
	operaciones_gravadas = models.DecimalField(max_digits=18,decimal_places=2,help_text="Operaciones Gravadas",default=0.00)
	operaciones_exoneradas = models.DecimalField(max_digits=18,decimal_places=2,help_text="operaciones Exoneradas",default=0.00)
	operaciones_inafecta = models.DecimalField(max_digits=18,decimal_places=2,help_text="Operaciones Inafectas",default=0.00)
	operaciones_gratuitas = models.DecimalField(max_digits=18,decimal_places=2,help_text="Operaciones Gratuitas",default=0.00)
	impuesto_bolsa = models.DecimalField(max_digits=18,decimal_places=2,help_text="Impuesto Bolsa",default=0.00)
	percepciones = models.DecimalField(max_digits=18,decimal_places=2,help_text="percepciones",default=0.00)
	retenciones = models.DecimalField(max_digits=18,decimal_places=2,help_text="Retenciones",default=0.00)
	total = models.DecimalField(max_digits=18,decimal_places=2,help_text="Total Venta")
	fecha_vencimiento = models.DateField(help_text="Fecha Vencimiento")
	forma_pago = models.ForeignKey(FormaPago,on_delete=models.CASCADE,blank=True, null=True)
	moneda = models.ForeignKey(Moneda,on_delete=models.CASCADE,blank=True, null=True)
	estado_operacion = models.ForeignKey(EstadoOperacion,on_delete=models.CASCADE,blank=True, null=True)
	estado_xml = models.BooleanField(blank=True,null=True,help_text="Estado XML")

class ComprobanteVentaDetalle(models.Model):
	id = models.BigAutoField(primary_key=True,verbose_name='ID')
	comprobante_venta = models.ForeignKey(ComprobanteVenta,on_delete=models.CASCADE,blank=True, null=True)
	producto = models.ForeignKey(Producto,on_delete=models.CASCADE,blank=True, null=True)
	cantidad = models.PositiveSmallIntegerField(help_text="Cantidad de Item")
	precio_venta_final =models.DecimalField(max_digits=18,decimal_places=2,help_text="Retenciones")
	importe = models.DecimalField(max_digits=18,decimal_places=2,help_text="Operaciones Gravadas")
	unidad_medida = models.ForeignKey(UnidadMedida,on_delete=models.CASCADE,blank=True, null=True)
	operaciones_gravadas = models.DecimalField(max_digits=18,decimal_places=2,help_text="Operaciones Gravadas",default=0.00)
	operaciones_exoneradas = models.DecimalField(max_digits=18,decimal_places=2,help_text="operaciones Exoneradas",default=0.00)
	operaciones_inafecta = models.DecimalField(max_digits=18,decimal_places=2,help_text="Operaciones Inafectas",default=0.00)
	operaciones_gratuitas = models.DecimalField(max_digits=18,decimal_places=2,help_text="Operaciones Gratuitas",default=0.00)
	impuesto_bolsa = models.DecimalField(max_digits=18,decimal_places=2,help_text="Impuesto Bolsa",default=0.00)
	percepciones = models.DecimalField(max_digits=18,decimal_places=2,help_text="percepciones",default=0.00)
	retenciones = models.DecimalField(max_digits=18,decimal_places=2,help_text="Retenciones",default=0.00)