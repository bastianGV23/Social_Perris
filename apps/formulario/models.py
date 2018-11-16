from django.db import models

# Create your models here.


class Contacto(models.Model):
    nombres = models.CharField(max_length=50)
    apPaterno = models.CharField(max_length=30)
    apMaterno = models.CharField(max_length=50)
    rut = models.CharField(max_length=9, primary_key=True)
    dvRut = models.CharField(max_length=1)
    fNacimiento = models.DateField()
    correo = models.CharField(max_length=50)
    telefono = models.IntegerField()

