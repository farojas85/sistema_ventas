from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class ClaseBigPk(models.Model):
    id = models.BigAutoField(primary_key=True,verbose_name="ID")

    class Meta:
        abstract = True