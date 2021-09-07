from django.shortcuts import render, redirect, get_object_or_404
from .models import producto,marca
from .forms import productoForms, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer, MarcaSerializer
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
class MarcaViewset(viewsets.ModelViewSet):
    queryset = marca.objects.all()
    serializer_class= MarcaSerializer

class ProductoViewset(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = producto.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)
        
        return productos 

def error_facebook(request):
    return render(request, 'registration/error_facebook.html')

def casa(request):
    productos = producto.objects.all()
    data = {
        'productos': productos
    }
    return render (request, 'home.html', data)


def agregar_producto(request):

    data ={
        'form': productoForms()
    }
    if request.method == 'POST':
        formulario = productoForms(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El producto se ha agregado Correctamente!!")
            return redirect(to="home")
        else:
            data["form"] = formulario
    return render(request, 'productos/agregar.html', data)

@permission_required('add.view_producto')
def listar_productos(request):
    productos = producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404


    data={
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'productos/listar.html', data)

#@permission_required('add.change_producto')
def modificar_productos(request, id):

    productos = get_object_or_404(producto, id=id)

    data={
        'Form': productoForms(instance=productos)
    }

    if request.method == 'POST':
        formulario=productoForms(data=request.POST, instance=productos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El producto se ha modificado Correctamente!!")
            return redirect(to="home")
        data["Form"] =formulario
    return render(request, 'productos/modificar.html', data)

#@permission_required('add.delete_producto')
def eliminar_producto(request, id):

    productos = get_object_or_404(producto, id=id)
    productos.delete()
    messages.success(request, "El producto se ha eliminado Correctamente!!")
    return redirect(to="home")

def registro(request):
    data={
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password2"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente!!")
            return redirect(to="home")

        else:
            data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def pronto(request):
    return render(request, "pronto.html")