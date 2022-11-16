from django.db import models

# Create your models here.
class cliente (models.Model):
    documento = models.IntegerField(primary_key=True,max_length=15)
    nombre = models.CharField(null=False,max_length=50)
    apellido = models.CharField(null=False,max_length=50)
    edad = models.PositiveSmallIntegerField(null=False,max_length=3)
    email = models.EmailField(blank=False)
    ciudad =models.CharField (max_length=30)
    genero = models.CharField (max_length=12)
    telefono = models.IntegerField (max_length=15)
    fechanacimiento =models.DateField(null=False)
    estadocivil = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


