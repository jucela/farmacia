from django.db import models

# Create your models here.
class presentacion(models.Model):
    id_presentacion=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)