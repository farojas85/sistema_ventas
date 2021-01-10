from django.db import models
from bases.models import ClaseModelo

# Create your models here.
#Modelo Departamento
class Departamento(models.Model):
    nombre= models.CharField(max_length=191,help_text='Descripción Departamento')

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name_plural= 'Departamentos'

class Provincia(models.Model):
    nombre = models.CharField(max_length=191, help_text="Descripción de Provincia")
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name_plural = 'Provincias'

class Distrito(models.Model):
    nombre = models.CharField(max_length=191, help_text="Descripción de Distrito")
    provincia = models.ForeignKey(Provincia,on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name_plural = 'Distritos'    

class TipoEmpresa(models.Model):
    codigo = models.CharField(max_length=2, help_text="Codigo Tipo Empresa")
    nombre = models.CharField(max_length=191, help_text="Descripción de Tipo Empresa")
    comentario = models.CharField(max_length=191, help_text="Comentario de Tipo Empresa",blank=True, null=True)
    
    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name_plural = 'TipoEmpresas'

class Empresa(ClaseModelo):
    tipo_empresa = models.ForeignKey(TipoEmpresa,on_delete=models.CASCADE,blank=True, null=True)
    ruc = models.CharField(max_length=11,help_text=" R.U.C. de Empresa",unique=True)
    razon_social = models.CharField(max_length=191,help_text="Razón Social Empresa")
    nombre_comercial = models.CharField(max_length=191, help_text="Nombre Comercial Empresa",blank=True, null=True)
    direccion_principal = models.CharField(max_length=191,help_text="Dirección Empresa")
    ubigeo = models.ForeignKey(Distrito,on_delete=models.CASCADE,blank=True, null=True)
    pagina_web = models.CharField(max_length=191,blank=True, null=True,help_text="URL / Dirección Web")
    usuario_sol = models.CharField(max_length=50,blank=True, null=True,help_text="Usuario Clave Sol")
    clave_sol = models.CharField(max_length=50, blank=True, null=True, help_text="COntraseña Clave Sol")
    certificado_pfx = models.BinaryField(blank=True, null=True,help_text='Archivo Certificado PFX',editable=True)
    fecha_caduca_certificado = models.DateField(blank=True, null=True,help_text="Fecha Caduca Certificado")
    certificado_zip = models.BinaryField(blank=True, null=True,help_text="Archivo Certificado Zip",editable=True)
    clave_certificado = models.CharField(max_length=50, blank=True, null=True,help_text="Contraseña Certificado")
    texto_encabezado = models.CharField(max_length=191, blank=True, null=True,help_text='Texto Encabezado')
    logo = models.BinaryField(blank=True, null=True,help_text="Logo Empresa",editable=True)
    imagen_pie_pagina = models.BinaryField(blank=True, null=True,help_text="Imagen de Pié de Página",editable=True)

    def __str__(self):
        return '{}'.format(self.razon_social)

    def save(self,*args, **kwargs):
        self.razon_social =self.razon_social.upper()
        self.nombre_comercial = self.nombre_comercial.upper()
        super(Empresa,self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural= 'Empresas'

class Sucursal(ClaseModelo):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,blank=True,null=True)
    nombre = models.CharField(max_length=191)
    direccion = models.CharField(max_length=191)
    referencia = models.CharField(max_length=191, blank=True, null=True)
    observacion = models.CharField(max_length=191, blank=True, null=True)
    ubigeo = models.ForeignKey(Distrito,on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre =self.nombre.upper()
        super(Sucursal,self).save()

    class Meta:
        verbose_name_plural= 'Sucursales'


class TipoAlmacen(ClaseModelo):
    nombre = models.CharField(max_length=191,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)
        
    def save(self):
        self.nombre =self.nombre.upper()
        super(TipoAlmacen,self).save()

    class Meta:
        verbose_name_plural= 'TipoAlmacenes'

class UnidadMedida(ClaseModelo):
    id_sunat = models.CharField(max_length=10,blank=True, null=True)
    nombre = models.CharField(max_length=191,blank=True, null=True)
    impresion= models.CharField(max_length=191, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre =self.nombre.upper()
        super(UnidadMedida,self).save()

    class Meta:
        verbose_name_plural= 'UnidadMedidas'

class Almacen(ClaseModelo):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE,blank=True,null=True)
    nombre = models.CharField(max_length=191)
    direccion = models.CharField(max_length=191)
    tipo_almacen =models.ForeignKey(TipoAlmacen, on_delete=models.CASCADE,blank=True,null=True)
    ubigeo = models.ForeignKey(Distrito,on_delete=models.CASCADE,blank=True, null=True)
    area = models.DecimalField(max_digits=18,decimal_places=2, blank=True, null=True)
    capacidad = models.DecimalField(max_digits=18,decimal_places=2, blank=True, null=True)
    unidad_medidad = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre =self.nombre.upper()
        super(Almacen,self).save()

    class Meta:
        verbose_name_plural= 'Almacenes'

class TipoPuntoVenta(ClaseModelo):
    nombre = models.CharField(max_length=191, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre =self.nombre.upper()
        super(TipoPuntoVenta,self).save()

    class Meta:
        verbose_name_plural= 'TipoPuntoVentas'

class PuntoVenta(ClaseModelo):
    tipo_punto_venta = models.ForeignKey(TipoPuntoVenta, on_delete=models.CASCADE,blank=True,null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE,blank=True,null=True)
    nombre_equipo = models.CharField(max_length=191)
 
    def __str__(self):
        return '{}'.format(self.nombre_equipo)

    class Meta:
        verbose_name_plural= 'PuntoVentas'

class Configuracion(models.Model):
    id = models.BigAutoField(primary_key=True,verbose_name='ID')
    nombre =  models.CharField(max_length=191,blank=True, null=True,unique=True)
    descripcion =  models.CharField(max_length=255,blank=True, null=True)
    observacion =  models.CharField(max_length=500,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name_plural= 'Configuraciones'

class ConfiguracionEmpresa(models.Model):
    id = models.BigAutoField(primary_key=True,verbose_name='ID')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,help_text="Modelo Empresa",blank=True,null = True)
    configuracion = models.ForeignKey(Configuracion, on_delete=models.CASCADE,help_text="Modelo Configuracion",blank=True,null = True)
    valor = models.CharField(max_length=191,blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    fecha_modificacion = models.DateTimeField(blank=True,null=True,auto_now=True)

    class Meta:
        verbose_name_plural= 'ConfiguracionEmpresas'