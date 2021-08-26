from .models import producto, marca
from rest_framework import serializers

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model= marca
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    nombre_marca = serializers.CharField(read_only=True, source="marca.nombre")
    Marca= MarcaSerializer(read_only=True)
    marca_id = serializers.PrimaryKeyRelatedField(queryset=marca.objects.all(), source="marca")
    nombre = serializers.CharField(required=True, min_length=3)

    def validate_nombre(self, value):
        existe = producto.objects.filter(nombre__iexact=value).exists()

        if existe:
            raise serializers.ValidationError("Este producto ya existe")

        return value

    class Meta:
        model = producto
        fields = '__all__'