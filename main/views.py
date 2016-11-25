# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from models import Usuario, Cliente, Restaurante, Platillo, Comentario
from forms import RestauranteForm, PlatilloForm, ComentarioForm
from django.template import RequestContext
from validator import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import *
from food_court.settings import STATIC_ROLS

def index(request):
	return render(request, 'main/index.html')

@login_required(login_url="/")
def perfil(request):

	# import pdb; pdb.set_trace()
	if User.objects.filter(id=request.user.id, groups = STATIC_ROLS['Cliente']).exists():   
		usuario = Cliente.objects.get(id=request.user.id)
		return render(request, 'main/perfil.html', {'user': usuario } )

	elif User.objects.filter(id=request.user.id, groups = STATIC_ROLS['Usuarios']).exists():
		usuario = Usuario.objects.get(id=request.user.id)
		return render(request, 'main/perfil.html', {'user': usuario } )

	else:
		return render(request, 'main/perfil.html')

@login_required(login_url="/")
def mapa(request):
	return render(request, 'main/mapa.html')

@login_required(login_url="/")
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

			return redirect('login')
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

			return redirect('login')
		else:
			return render(request, 'main/registrar-clientes.html', {'error': validators.getMessage() } )
		# Agregar el usuario a la base de datos
	return render( request, 'main/registrar-clientes.html' )


def login(request):

	if request.method == 'POST':

		validators = FormLoginValidator(request.POST)

		if validators.is_valid():

			auth.login(request, validators.acceso)  # Crear una sesion
			return redirect('/principal')

		else:
			return render(request, 'main/login.html', {'error': validators.getMessage()} )

	return render(request, 'main/login.html' )

@login_required(login_url="/")
def logout(request):
	auth.logout(request)
	return redirect("/")    

@login_required(login_url="/")
def principal(request):
	return render(request, 'main/principal.html')

@login_required(login_url="/")
def restaurante(request):
	if request.user.groups.filter(id = 2 ).exists():
		restaurante = Restaurante.objects.all()
	else:
		restaurante = Restaurante.objects.filter( restaurante_cliente_id = request.user.id )
	return render(request, 'main/restaurante.html', { 'restaurante': restaurante })

@login_required(login_url="/")
def add_restaurante(request):
	if request.method == "POST":
		form = RestauranteForm(request.POST, request.FILES)
		if form.is_valid():
			restaurante = form.save(commit=False)
			restaurante.restaurante_cliente_id = request.user.id
			# restaurante.image = request.FILES.get('imagen')
			restaurante.save()
			return redirect('restaurante-detalle', pk=restaurante.pk)
	else:
		form = RestauranteForm()
	return render(request, 'main/add-restaurante.html', { 'form' : form } )

class RestauranteCreateView(CreateView):
	model = Restaurante
	template_name = 'main/add-menu.html'
	success_message = 'Exactly'
	form_class = RestauranteForm

	def get_success_url(self):
		return reverse('list-menu')

	def form_valid(self, form):
	    """
	    If the form is valid, save the associated model.
	    """
	    self.object = form.save()
	    return super(ModelFormMixin, self).form_valid(form)

@login_required(login_url="/")
def edit_restaurante(request, pk):
	restaurante = get_object_or_404(Restaurante, pk=pk)
	if request.method == "POST":
		# import pdb; pdb.set_trace();
		form = RestauranteForm(request.POST, instance=restaurante)
		if form.is_valid():
			restaurante = form.save(commit=False)
			restaurante.restaurante_cliente_id = request.user.id
			restaurante.image = request.FILES.get('imagen')
			restaurante.save()
			return redirect('restaurante-detalle', pk=restaurante.pk)
	else:
		form = RestauranteForm(instance=restaurante)
	return render(request, 'main/edit-restaurante.html', {'form': form, 'restaurante':restaurante})

@login_required(login_url="/")
def delete_restaurante(request, pk):
	restaurante = get_object_or_404(Restaurante, pk=pk)
	restaurante.delete()
	return redirect('restaurante')

@login_required(login_url="/")
def restaurante_detail(request, pk):
	restaurante = get_object_or_404(Restaurante, pk=pk)
	return render(request, 'main/restaurante-detail.html', {'restaurante': restaurante })

@login_required(login_url="/")
def menu_list(request, pk):
    if request.user.groups.filter(id = 1 ).exists():
        restaurante = Restaurante.objects.get(pk = pk)
    elif request.user.groups.filter(id = 2 ).exists():
        # import pdb; pdb.set_trace()
        restaurante1 = Restaurante.objects.get(pk = pk)
        restaurante = Platillo.objects.filter(restaurante_platillo_id = restaurante1.id)
	return render(request, 'main/menu.html', { 'restaurante': restaurante })

@login_required(login_url="/")
def add_menu(request):
	
	restaurante = Restaurante.objects.filter(id=request.user.id)
	if request.method == "POST":
		form = PlatilloForm(request.user, request.POST)
		if form.is_valid():
			menu = form.save(commit=False)
			menu.save()
			return redirect('list-menu')
	else:
		form = PlatilloForm(request.user)
	return render(request, 'main/add-menu.html', { 'form' : form } )

@login_required(login_url="/")
def edit_menu(request, pk):
	menu = get_object_or_404(Platillo, pk=pk)
	if request.method == "POST":
		form = PlatilloForm(request.POST, instance=menu)
		if form.is_valid():
			menu = form.save(commit=False)
			menu.save()
			return redirect('list-menu')
	else:
		form = PlatilloForm(instance=menu)
	return render(request, 'main/edit-menu.html', {'form': form, 'menu':menu})

class MenuCreateView(CreateView):
	model = Platillo
	template_name = 'main/edit-menu.html'
	success_message = 'Exactly'
	form_class = PlatilloForm

	def get_form_kwargs(self):
		kwargs = super(MenuCreateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

	def get_success_url(self):
		return reverse('list-menu')

class MenuUpdateView(UpdateView):
	model = Platillo
	template_name = 'main/edit-menu.html'
	success_message = 'Exactly'
	form_class = PlatilloForm

	def get_form_kwargs(self):
		kwargs = super(MenuUpdateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

	def get_success_url(self):
		return reverse('list-menu')

@login_required(login_url="/")
def delete_menu(request, pk):
    menu = get_object_or_404(Platillo, pk=pk)
    menu.delete()
    return redirect('restaurante')

# <----------------------- Comentarios --------------------->

@login_required(login_url="/")
def add_comment(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    # import pdb; pdb.set_trace()
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.restaurante_id = restaurante.id
            comment.save()
            return redirect('restaurante-detalle', pk=restaurante.pk)
    else:
        form = ComentarioForm()
    return render(request, 'main/add_comment.html', {'form': form})    

@login_required(login_url="/")
def comment_remove(request, pk):
    comment = get_object_or_404(Comentario, pk=pk)
    restaurante_id = comment.restaurante.id
    comment.delete()
    return redirect('restaurante-detalle', pk=restaurante_id)    
