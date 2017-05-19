from django.db import models

# Create your models here.
class Cliente(models.Model):
    sexo_choices = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),

    )
    id_cliente=models.IntegerField(primary_key=True)
    nombres=models.CharField(max_length=50)
    apellidos= models.CharField(max_length=50)
    dni= models.CharField(max_length=8)
    sexo= models.CharField(max_length=50,choices=sexo_choices)
    fnacimiento=models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono= models.CharField(max_length=15)
    correo= models.EmailField(max_length=50)
    