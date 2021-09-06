from django import forms
from django.forms import fields
from .models import producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError
from bootstrap_datepicker_plus import DatePickerInput

class productoForms(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    username = forms.CharField(min_length=3, max_length=100)
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])
    precio = forms.IntegerField(required=False, min_value=1, max_value=3000000)

    def clean_nombre(self):
        nombre= self.cleaned_data["nombre"]
        existe = producto.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este nombre ya existe")
        return nombre



    class Meta:
        model= producto
        fields='__all__'

        widgets ={
            "fecha_fabricacion": DatePickerInput(format='%d/%m/%Y')
        }

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1"]