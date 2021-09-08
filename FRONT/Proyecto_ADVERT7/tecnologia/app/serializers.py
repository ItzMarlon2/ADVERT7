#from django.contrib.auth.models import User
from .models import producto, Categoria
from rest_framework import serializers
from django.contrib.auth.models import User

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields = '__all__'

#class UserSerializer(serializers.ModelSerializer):
    #class Meta:
     #   model= User
      #  fields = ['username']

class ProductoSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.CharField(read_only=True, source="categoria.nombre")
    categoria= CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source="categoria")
    #nombre_users = serializers.CharField(read_only=True, source="User.username")
    #users= UserSerializer(read_only=True) vnbc
    #User_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source="user")
    nombre = serializers.CharField(required=True, min_length=3)
    username = serializers.CharField(required=True, min_length=3)
    precio = serializers.IntegerField(required=False)
    telefono = serializers.CharField(required=False)

    class Meta:
        model = producto
        fields = '__all__'