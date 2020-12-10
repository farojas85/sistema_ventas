from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from bases.models import ClaseModelo
from emp.models import Empresa

# Create your models here.
class TipoDocumento(ClaseModelo):
    tipo = models.CharField(max_length=2, blank=True, null=True,help_text='Código Tipo Documento')
    nombre_corto = models.CharField(max_length=191,blank=True, null=True,help_text="Descripción Corta")
    nombre_largo = models.CharField(max_length=191,blank=True, null=True,help_text="Descripción Larga")
    longitud = models.PositiveSmallIntegerField(help_text="Longitud Documento")
    fecha_eliminada = models.DateTimeField(blank=True, null=True,help_text="Fecha Eliminada")

    class Meta:
        verbose_name_plural='tipo_documentos'

    def __str__(self):
        return '{}'.format(self.nombre_corto)

class Sexo(models.Model):
    nombre = models.CharField(max_length=191,help_text="Descripción Sexo")
    class Meta:
        verbose_name_plural='sexos'
    
    def __str__(self):
        return '{}'.format(self.nombre)

class Persona(ClaseModelo):
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, blank=True, null=True)
    numero_documento = models.CharField(max_length=15,help_text="Número Documento")
    nombres = models.CharField(max_length=191,help_text="Nombres")
    apellidos = models.CharField(max_length=191,help_text='Apellidos')
    telefono = models.CharField(max_length=50,blank=True, null=True,help_text="Teléfono")
    direccion = models.CharField(max_length=191,blank=True, null=True,help_text="Dirección")
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE, blank=True, null=True,help_text="Sexo Persona")
    class Meta:
        verbose_name_plural= 'personas'

    def __str__(self):
        return '{0} {1}'.format(self.nombres,self.apellidos)

class UsuarioManager(BaseUserManager):
    def create_user(selft,persona,nombre,correo,password=None,**extra_fields):
        if not nombre:
            raise ValueError('Debe Ingresar Nombre de Usuario')

        usuario  = self.model(
            persona = persona,
            nombre=nombre,
            correo = self.normalize_email(correo)
        )

        usuario.set_password(password)
        usuario.save()

        return usuario

class Usuario(AbstractBaseUser):
    persona =  models.OneToOneField(Persona, on_delete=models.CASCADE,help_text="Persona Usuario",blank=True,null = True)
    nombre = models.CharField(max_length=191,unique=True,help_text="Nombre Usuario")
    correo = models.EmailField(help_text="Correo Electrónico", max_length=191,unique=True,blank=True, null=True)
    imagen  = models.ImageField(max_length=191,help_text="Imagen de Perfil",upload_to="media/imagen/", blank=True,null=True)
    estado = models.BooleanField(default=True)
    fecha_creada = models.DateTimeField(auto_now_add=True)
    fecha_modificada = models.DateTimeField(auto_now=True)
    fecha_eliminada = models.DateTimeField(help_text="Fecha Eliminada",blank=True, null=True)
    objects = UsuarioManager()

    USERNAME_FIELD= 'nombre'
    REQUIRED_FIELD=['nombre','correo']

    def __str__(self):
        return '{}'.format(self.nombre)
    
    def get_full_name(selft):
        return self.nombre
    
    def get_short_name(selft):
        return self.nombre

    @property
    def is_active(self):
        return self.estado

class Acceso(model.Models):
    nombre = models.CharField(max_length=191,help_text="Nombre de Acceso")
    slug = models.CharField(help_text="L", max_length=50)
    descripcion = models.CharField(help_text="Descripción de Acceso", max_length=191, blank=True, null=True)
class Role(model.Models):
    nombre: