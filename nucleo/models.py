from django.db import models
#autores uziel y brenda

class Cliente(models.Model):
     
    usuario = models.CharField(max_length=100)

    apellido = models.CharField(max_length=100)

    correo = models.EmailField(blank= True , null = True)

    password = models.CharField(max_length=100)

    telefono =  models.CharField(max_length=10)

    adiccion = models.CharField(max_length=50)

    def __str__ (self):
        return f"{self.usuario} {self.apellido}"
