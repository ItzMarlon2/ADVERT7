from django.contrib import admin
from .models import Categoria, producto
from .forms import productoForms
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "categoria", "fecha_fabricacion"]
    list_editable =["precio"]
    search_fields =["nombre"]
    list_filter =["categoria", "nuevo"]
    form = productoForms

admin.site.register(Categoria)
admin.site.register(producto, ProductoAdmin)