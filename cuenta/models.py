from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from bases.models import ClaseModelo,ClaseBigPk
from emp.models import Empresa

# Create your models here.
class Menu(models.Model):
    nombre = models.CharField(max_length=191,help_text="Nombre del Menú")
    enlace = models.CharField(max_length=191,help_text="Ruta Menú")
    icono = models.CharField(max_length=191, blank=True, null=True,help_text="Icono del Menú")
    padre = models.IntegerField(default=0,help_text="Padre del Menú")
    orden = models.SmallIntegerField(blank=True, null=True,help_text="Orden de menú")
    estado = models.BooleanField(default=True)
    fecha_creada = models.DateTimeField(auto_now_add=True)
    fecha_modificada = models.DateTimeField(auto_now=True)
    fecha_eliminada = models.DateTimeField(help_text="Fecha Eliminada",blank=True, null=True)

    class Meta:
        verbose_name_plural='menus'

    def __str__(self):
        return '{}'.format(self.nombre)

class Permiso(models.Model):
    nombre = models.CharField(max_length=191,help_text="Nombre de Acceso")
    slug = models.CharField(help_text="Ruta Amigable Acceso", max_length=191)
    descripcion = models.CharField(help_text="Descripción de Acceso", max_length=191, blank=True, null=True)
    estado = models.BooleanField(default=True)
    fecha_creada = models.DateTimeField(auto_now_add=True)
    fecha_modificada = models.DateTimeField(auto_now=True)
    fecha_eliminada = models.DateTimeField(help_text="Fecha Eliminada",blank=True, null=True)

    class Meta:
        verbose_name_plural='permisos'

    def __str__(self):
        return '{}'.format(self.nombre)

class Acceso(models.Model):
    nombre = models.CharField(max_length=191,help_text="Nombre de Acceso")
    slug = models.CharField(help_text="Ruta Amigable Acceso", max_length=191)
    descripcion = models.CharField(help_text="Descripción de Acceso", max_length=191, blank=True, null=True)
    estado = models.BooleanField(default=True)
    fecha_creada = models.DateTimeField(auto_now_add=True)
    fecha_modificada = models.DateTimeField(auto_now=True)
    fecha_eliminada = models.DateTimeField(help_text="Fecha Eliminada",blank=True, null=True)

    class Meta:
        verbose_name_plural='accesos'

    def __str__(self):
        return '{}'.format(self.nombre)

class Role(models.Model):
    nombre = models.CharField(max_length=191, blank=True, null=True,help_text="Nombre de Rol")
    slug = models.CharField(max_length=191, blank=True, null=True,help_text="Ruta Amigable Rol")
    descripcion = models.CharField(max_length=191, blank=True, null=True,help_text="Descripción de Rol")
    acceso = models.ForeignKey(Acceso, on_delete=models.CASCADE,help_text="Persona Usuario",blank=True,null = True)
    estado = models.BooleanField(default=True)
    fecha_creada = models.DateTimeField(auto_now_add=True)
    fecha_modificada = models.DateTimeField(auto_now=True)
    fecha_eliminada = models.DateTimeField(help_text="Fecha Eliminada",blank=True, null=True)
    permisos = models.ManyToManyField(Permiso)
    menus = models.ManyToManyField(Menu)

    class Meta:
        verbose_name_plural='roles'

    def __str__(self):
        return '{}'.format(self.nombre)

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
    def create_user(selft,empresa,persona,username,email,password,**extra_fields):
        if not username:
            raise ValueError('Debe Ingresar Nombre de Usuario')

        usuario  = self.model(
            empresa = empresa,
            persona = persona,
            username=username,
            email = self.normalize_email(email)
        )

        usuario.set_password(password)
        usuario.save()

        return usuario

class Usuario(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True,verbose_name='ID')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,help_text="Persona Usuario",blank=True,null = True)
    persona =  models.OneToOneField(Persona, on_delete=models.CASCADE,help_text="Persona Usuario",blank=True,null = True)
    username = models.CharField(max_length=191,unique=True,help_text="Nombre Usuario")
    email = models.EmailField(help_text="Correo Electrónico", max_length=191,unique=True,blank=True, null=True)
    imagen  = models.ImageField(max_length=191,help_text="Imagen de Perfil",upload_to="media/imagen/", blank=True,null=True)
    estado = models.BooleanField(default=True)
    fecha_creada = models.DateTimeField(auto_now_add=True)
    fecha_modificada = models.DateTimeField(auto_now=True)
    fecha_eliminada = models.DateTimeField(help_text="Fecha Eliminada",blank=True, null=True)
    objects = UsuarioManager()
    roles = models.ManyToManyField(Role)

    USERNAME_FIELD= 'username'
    REQUIRED_FIELD=['username','email']
    
    def __str__(self):
        return '{}'.format(self.username)
    
    def get_user(self):
        return self.usename
        
    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username

    @property
    def is_active(self):
        return self.estado