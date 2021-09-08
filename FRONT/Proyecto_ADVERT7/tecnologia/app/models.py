from django.db import models
#from django.contrib.auth.models import User
# Create your models here.
class Categoria(models.Model):
    nombre= models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class producto(models.Model):
    nombre=models.CharField(max_length=50)
    username=models.CharField(max_length=100)
    precio=models.IntegerField(null=True)
    descripcion=models.TextField()
    nuevo=models.BooleanField()
    categoria=models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fecha_fabricacion=models.DateField(auto_now=True)
    telefono=models.CharField(null=True, max_length=10)
    imagen=models.ImageField(upload_to="productos", null="True")
    #users=models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre

