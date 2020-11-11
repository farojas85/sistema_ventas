from django.db import models
from bases.models import ClaseModelo

# Create your models here.
#Modelo Departamento
class Departamento(models.Model):
    codigo= models.CharField(max_length=2,help_text="Código Departamento")
    nombre= models.CharField(max_length=191,help_text='Descripción Departamento')

    class Meta:
        verbose_name_plural= 'Departamentos'

class Provincia(models.Model):
    codigo = models.CharField(max_length=4, help_text="Codigo Provincia")
    nombre = models.CharField(max_length=191, help_text="Descripción de Provincia")
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Provincias'

class Distrito(models.Model):
    codigo = models.CharField(max_length=6, help_text="Codigo Distrito")
    nombre = models.CharField(max_length=191, help_text="Descripción de Distrito")
    provincia = models.ForeignKey(Provincia,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Distritos'   

class Empresa(ClaseModelo):
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

    def save(self):
        self.razon_social =self.razon_social.upper()
        self.nombre_comercial = self.nombre_comercial.upper()
        super(Empresa,self).save()

    class Meta:
        verbose_name_plural= 'Empresas' 

# class Sucursal(ClaseModelo):
#     empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
#     nombre = models.CharField(max_length=191)
#     direccion = models.CharField(max_length=191)