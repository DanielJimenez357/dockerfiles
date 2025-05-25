from django.db import models
from usuarios_app.models import Usuario

# Create your models here.

class Alojamiento(models.Model):

    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    propietario=models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name="propietario")
    alquileres=models.ManyToManyField(Usuario, through="Alquiler", related_name="alquileres")

class Alquiler(models.Model):

    cliente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name="cliente")
    alojamiento = models.ForeignKey(Alojamiento, on_delete=models.SET_NULL, null=True, blank=True, related_name = "alojamientos")
    desde = models.DateField()
    hasta = models.DateField()
    comentario = models.CharField(max_length=200, null=True, blank=True)

