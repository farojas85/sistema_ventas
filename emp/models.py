from django.db import models
from bases.models import ClaseModelo

# Create your models here.
class Empresa(ClaseModelo):
    ruc = models.CharField(max_length=11,help_text=" R.U.C. de Empresa",unique=True)
    razon_social = models.CharField(max_length=191,help_text="Razón Social Empresa")
    nombre_comercial = models.CharField(max_length=191, help_text="Nombre Comercial Empresa",blank=True, null=True)
    direccion_principal = models.CharField(max_length=191,help_text="Dirección Empresa")
    ubigeo = models.CharField(max_length=191,help_text="Ubigeo Empresa")
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