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


    class Meta:
        model= producto
        fields = ['nombre', 'username', 'precio', 'descripcion', 'nuevo', 'marca', 'imagen']

        widgets ={
            "fecha_fabricacion": DatePickerInput(format='%d/%m/%Y')
        }

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1"]