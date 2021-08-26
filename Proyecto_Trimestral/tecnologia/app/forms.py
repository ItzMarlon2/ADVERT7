from django import forms
from django.forms import fields
from .models import contacto, producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError
from bootstrap_datepicker_plus import DatePickerInput

class Contacto_form(forms.ModelForm):

    class Meta:
        model = contacto
        #fields =["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields='__all__'



class productoForms(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])
    precio = forms.IntegerField(min_value=1, max_value=3000000)

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