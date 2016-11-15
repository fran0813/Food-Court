# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from models import *
from forms import RestauranteForm
from django.template import RequestContext
from validator import *

def index(request):
    return render(request, 'main/index.html')

def perfil(request):
    return render(request, 'main/perfil.html')

def mapa(request):
    return render(request, 'main/mapa.html')

def contacto(request):
    return render(request, 'main/contactenos.html')

def registrar_usuario(request):

    error = False
    if request.method == 'POST':
        validators = FormRegistroValidator(request.POST)
        validators.required = ['nombre', 'apellidos', 'email', 'documento', 'username', 'password1']

        if validators.is_valid():
            usuario = User()
            usuario.first_name = request.POST['nombre']
            usuario.last_name = request.POST['apellidos']
            usuario.email = request.POST['email']
            usuario.username = request.POST['username']
            usuario.password = make_password(request.POST['password1'])
            usuario.is_active = True
            grupo = Group.objects.get(name="Usuarios")  
            usuario.save()
            usuario.groups.add(grupo)
            usuario.save()

            myusuario = Usuario()
            myusuario.id = usuario
            myusuario.documento = request.POST['documento']
            myusuario.direccion = request.POST['direccion']
            myusuario.telefono = request.POST['telefono']
            myusuario.save()

            return render(request, 'main/login.html', {'success': True})
        else:
            return render(request, 'main/registrar.html', {'error': validators.getMessage() } )
        # Agregar el usuario a la base de datos
    return render( request, 'main/registrar.html' )

def registrar_cliente(request):

    error = False
    if request.method == 'POST':
        validators = FormRegistroValidator(request.POST)
        validators.required = ['nombre', 'apellidos', 'email', 'documento', 'username', 'password1']

        if validators.is_valid():
            usuario = User()
            usuario.first_name = request.POST['nombre']
            usuario.last_name = request.POST['apellidos']
            usuario.email = request.POST['email']
            usuario.username = request.POST['username']
            usuario.password = make_password(request.POST['password1'])
            usuario.is_active = True
            grupo = Group.objects.get(name="Cliente") # carga el grupo
            usuario.save()
            usuario.groups.add(grupo)
            usuario.save()

            myusuario = Cliente()
            myusuario.id = usuario
            myusuario.documento = request.POST['documento']
            myusuario.direccion = request.POST['direccion']
            myusuario.telefono = request.POST['telefono']
            myusuario.save()

            return render(request, 'main/login.html', {'success': True})
        else:
            return render(request, 'main/registrar-clientes.html', {'error': validators.getMessage() } )
        # Agregar el usuario a la base de datos
    return render( request, 'main/registrar-clientes.html' )


def login(request):

    if request.method == 'POST':

        validators = FormLoginValidator(request.POST)

        if validators.is_valid():

            auth.login(request, validators.acceso)  # Crear una sesion
            return HttpResponseRedirect('/principal')

        else:
            return render(request, 'main/login.html', {'error': validators.getMessage()} )

    return render(request, 'main/login.html' )

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")    

def principal(request):
    return render(request, 'main/principal.html')
       
def restaurante(request):
    restaurante = Restaurante.objects.filter()
    return render(request, 'main/restaurante.html', { 'restaurante': restaurante })

def add_restaurante(request):
    if request.method == "POST":
        form = RestauranteForm(request.POST)
        if form.is_valid():
            restaurante = form.save(commit=False)
            restaurante.restaurante_cliente_id = request.user.id
            restaurante.save()
            return redirect('restaurante-detalle', pk=restaurante.pk)
    else:
        form = RestauranteForm()
    return render(request, 'main/add-restaurante.html', { 'form' : form } )

def restaurante_detail(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    return render(request, 'main/restaurante-detail.html', {'restaurante': restaurante })