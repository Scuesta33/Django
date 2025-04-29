from django.db import models

class Clientes (models.model):
    nombre=models.CharField(max_length=50)
    fecha=models.DateTimeField()
    nombreEmpleado= models.ForeignKey(Empleados)

    def__str__(self):
        return self.nombre



class Empleados(models.model):
    nombre=models.CharField(max_length=50)
    fecha=models.DateTimeField()
