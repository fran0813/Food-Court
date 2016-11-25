from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
	id = models.OneToOneField(User, primary_key=True, db_column='idusuarios')
	telefono = models.IntegerField( null = True, db_column='telefono' )
	direccion = models.CharField(max_length = 45, db_column='direccion')
	documento = models.IntegerField( db_column='documento')

	class Meta:
		db_table = 'usuarios'
		managed  = False

	def __str__(self):
		return '{}'.format(self.id)

class Cliente(models.Model):
	id = models.OneToOneField(User, primary_key=True, db_column='idclientes')
	telefono = models.IntegerField( null = True, db_column='telefono' )
	direccion = models.CharField(max_length = 145, db_column='direccion')
	documento = models.IntegerField( db_column='documento')

	class Meta:
		db_table = 'clientes'
		managed  = False

	def __str__(self):
		return '{}'.format(self.id)

class Restaurante(models.Model):
	id = models.AutoField( primary_key=True, db_column='idrestaurante')
	nombre = models.CharField(max_length = 45, db_column='nombre')
	telefono = models.CharField(max_length = 45, db_column='telefono')
	direccion = models.CharField(max_length = 45, db_column='direccion')
	sitioweb = models.CharField(max_length = 45, db_column='sitioweb')
	restaurante_cliente = models.ForeignKey(Cliente , db_column='restaurante_cliente')
	informacion = models.TextField( db_column='informacion')
	image = models.ImageField( upload_to = 'photos/' , default="../static/my/img/img4.jpg", db_column='imagen')


	class Meta:
		db_table = 'restaurante'
		managed  = False

	def __str__(self):
		return '{}'.format(self.nombre)

class Comentario(models.Model):
	id = models.AutoField( primary_key=True, db_column='idusuarios_clientes')
	usuario = models.ForeignKey(Usuario, db_column='usuarios_restaurante_usuarios')
	restaurante = models.ForeignKey(Restaurante , related_name='comments', db_column='usuarios_restaurante_restaurante')
	comentarios = models.TextField(db_column='comentarios')

	class Meta:
		db_table = 'usuarios_restaurante'
		managed  = False

class Platillo(models.Model):
	id = models.AutoField( primary_key=True, db_column='idplatillos')
	nombre = models.CharField(max_length = 45, db_column='nombre')
	precio = models.IntegerField( db_column='precio')
	detalle = models.CharField(max_length = 100, db_column='detalle')
	restaurante_platillo = models.ForeignKey(Restaurante , db_column='restaurante_platillos')


	class Meta:
		db_table = 'platillos'
		managed  = False