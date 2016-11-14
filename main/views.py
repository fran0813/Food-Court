from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from models import *
from django.template import RequestContext
from validator import *

def index(request):
    return render(request, 'main/index.html')

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
            # perfil = Group.objects.get(name="Estudiantes")  # carga un perfil de tipo usuario
            usuario.save()
            # usuario.groups.add(perfil)
            # usuario.save()

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
            # perfil = Group.objects.get(name="Estudiantes")  # carga un perfil de tipo usuario
            usuario.save()
            # usuario.groups.add(perfil)
            # usuario.save()

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

def principal(request):
    return render(request, 'main/principal.html')
