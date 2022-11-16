from django.db import models

# Create your models here.
class cliente (models.Model):
    documento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(null=False,max_length=50)
    edad = models.PositiveSmallIntegerField(null=False)
    email = models.EmailField(blank=False,null=False)
    ciudad =models.CharField (max_length=30,null=False)
    genero = models.CharField (max_length=12,null=False)
    telefono = models.IntegerField (null=False)
    fechanacimiento =models.DateField(null=False)
    estadocivil = models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.nombre

class Citas (models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.PROTECT)
    especialidad = models.CharField(null=False,max_length=15)
    especialista = models.CharField(null=False,max_length=15,default='Desconoce')
    fecha = models.DateField(null=False)
    lugar = models.CharField(null=False,max_length=15)
    hora = models.TimeField()
    observaciones = models.CharField(null=False, max_length=40)

    def __str__(self):
        return self.especialidad




