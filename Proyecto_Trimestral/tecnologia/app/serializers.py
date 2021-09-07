#from django.contrib.auth.models import User
from .models import producto, marca
from rest_framework import serializers
from django.contrib.auth.models import User

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model= marca
        fields = '__all__'

#class UserSerializer(serializers.ModelSerializer):
    #class Meta:
     #   model= User
      #  fields = ['username']

class ProductoSerializer(serializers.ModelSerializer):
    nombre_marca = serializers.CharField(read_only=True, source="marca.nombre")
    Marca= MarcaSerializer(read_only=True)
    marca_id = serializers.PrimaryKeyRelatedField(queryset=marca.objects.all(), source="marca")
    #nombre_users = serializers.CharField(read_only=True, source="User.username")
    #users= UserSerializer(read_only=True)
    #User_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source="user")
    nombre = serializers.CharField(required=True, min_length=3)
    username = serializers.CharField(required=True, min_length=3)
    precio = serializers.IntegerField(required=False)

    class Meta:
        model = producto
        fields = '__all__'