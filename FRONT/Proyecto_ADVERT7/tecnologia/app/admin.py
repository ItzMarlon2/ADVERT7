from django.contrib import admin
from .models import marca, producto
from .forms import productoForms
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "marca", "fecha_fabricacion"]
    list_editable =["precio"]
    search_fields =["nombre"]
    list_filter =["marca", "nuevo"]
    form = productoForms

admin.site.register(marca)
admin.site.register(producto, ProductoAdmin)