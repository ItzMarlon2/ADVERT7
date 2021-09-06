from django.urls import path, include
from .views import casa, galeria, agregar_producto, listar_productos, \
    modificar_productos, eliminar_producto, registro, ProductoViewset, MarcaViewset, \
    error_facebook, pronto
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('marca', MarcaViewset)

urlpatterns = [
    path('', casa, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('agregar/', agregar_producto, name="agregar"),
    path('listar/', listar_productos, name="listar"),
    path('modificar/<id>/', modificar_productos, name="modificar"),
    path('eliminar/<id>/', eliminar_producto, name="eliminar"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
    path('error-facebook/', error_facebook, name="error_facebook"),
    path('pronto/', pronto, name="pronto"),
]