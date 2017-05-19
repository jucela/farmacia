from django.db import models

# Create your models here.class #
class proveedor(models.Model):
    id_proveedor=models.IntegerField(primary_key=True)
    ruc = models.CharField(max_length=11)
    razon_social = models.CharField(max_length=100)
    nombre=models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=50)


    def __str__(self):
        return '{}'.format(self.nombre)