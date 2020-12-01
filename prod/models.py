from django.db import models
from bases.models import ClaseModelo
from emp.models import Empresa

# Create your models here.
#Modelo Departamento
class Categoria(ClaseModelo):
    nombre= models.CharField(max_length=191,help_text='Descripción Producto')
    imagen= models.BinaryField(blank=True, null=True,help_text="Imagen Producto",editable=True)
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE,blank=True, null=True)
    class Meta:
        verbose_name_plural= 'categorias'

class TipoProducto(ClaseModelo):
    nombre= models.CharField(max_length=191,help_text='Descripción Tipo Producto')
    class Meta:
        verbose_name_plural= 'tipo_productos'

class Marca(ClaseModelo):
    nombre= models.CharField(max_length=191,help_text='Descripción Tipo Producto')
    class Meta:
        verbose_name_plural= 'marcas'

class Producto(ClaseModelo):
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE, blank=True, null=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,blank=True, null=True)
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE,blank=True, null=True)
    numero_parte = models.CharField(max_length=50, help_text="Descripción Número parte",blank=True, null=True)
    codigo_proveedor = models.CharField(max_length=50,help_text="Código de Proveedor",blank=True, null=True)
    codigo_interno = models.CharField(max_length=50,help_text="Código Interno",blank=True, null=True)
    codigo_sunat = models.CharField(max_length=50,help_text="Código Producto Sunat",blank=True, null=True)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE,blank=True, null=True)
    nombre= models.CharField(max_length=191,help_text='Descripción de Producto',unique=True)
    detalle = models.CharField(max_length=255,help_text="Detalle de Producto",blank=True, null=True)
    imagen= models.BinaryField(blank=True, null=True,help_text="Imagen Producto",editable=True)
    afecto_igv = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural= 'productos'