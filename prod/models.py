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
        
    def __str__(self):
        return '{}'.format(self.nombre)

class TipoProducto(ClaseModelo):
    nombre= models.CharField(max_length=191,help_text='Descripción Tipo Producto')

    class Meta:
        verbose_name_plural= 'tipo_productos'

    def __str__(self):
        return '{}'.format(self.nombre)

class Marca(ClaseModelo):
    nombre= models.CharField(max_length=191,help_text='Descripción Tipo Producto')
    class Meta:
        verbose_name_plural= 'marcas'

    def __str__(self):
        return '{}'.format(self.nombre)

class Producto(ClaseModelo):
    id = models.BigAutoField(primary_key=True,verbose_name='ID')
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE, blank=True, null=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,blank=True, null=True)
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE,blank=True, null=True)
    numero_parte = models.CharField(max_length=50, help_text="Descripción Número parte",blank=True, null=True)
    codigo_proveedor = models.CharField(max_length=50,help_text="Código de Proveedor",blank=True, null=True)
    codigo_interno = models.CharField(max_length=50,help_text="Código Interno",blank=True, null=True)
    codigo_sunat = models.CharField(max_length=50,help_text="Código Producto Sunat",blank=True, null=True)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE,blank=True, null=True)
    nombre= models.CharField(max_length=191,help_text='Descripción de Producto',unique=True)
    detalle = models.TextField(max_length=255,help_text="Detalle de Producto",blank=True, null=True)
    imagen= models.ImageField(blank=True, null=True,help_text="Imagen Producto",editable=True,upload_to="productos/images/")
    afecto_igv = models.BooleanField(blank=True, null=True,help_text="IGV Afecto")

    class Meta:
        verbose_name_plural= 'productos'
    
    def __str__(self):
        return '{}'.format(self.nombre)