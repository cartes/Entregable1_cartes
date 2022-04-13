from django.db import models

# Create your models here.
class User(models.Model):
    nombres = models.CharField(max_length=55)
    apellidos = models.CharField(max_length=55)
    role = models.IntegerField()

class RoleUsuario(models.Model):
    nombre = models.CharField(max_length=60)
    role_number = models.IntegerField()

class Producto(models.Model):
    user_id = models.IntegerField()
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.FloatField()
    fecha_publicacion = models.DateField()

    def __str__(self):
        return f"Producto: {self.titulo}"