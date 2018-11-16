from django.db import models
from apps.formulario.models import Contacto
from apps.rescate.models import perrito,Estado
# Create your models here.
default_D = 1
class Adopcion(models.Model):
    rut = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    id_perro = models.OneToOneField(perrito,on_delete=models.CASCADE,unique = True)
    id_estado = models.ForeignKey(Estado,on_delete=models.CASCADE,default=default_D)