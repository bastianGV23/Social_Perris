from django.db import models
from apps.formulario.models import Contacto

# Create your models here.
class Estado(models.Model):
    estado = models.CharField(max_length=50,blank=True, null=True)
    def __str__(self):
        return self.estado

default_D = 1       
class perrito(models.Model):
    nombrePerro = models.CharField(max_length=50)
    razaP = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    imagen =  models.FileField(max_length=None, upload_to='media')
    estado = models.OneToOneField(Estado, on_delete=models.CASCADE,null = True,default=default_D)

    def __str__(self):
        return self.nombrePerro + ' ' + self.razaP + ' ' + self.descripcion 
