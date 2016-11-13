from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
	id = models.OneToOneField(User, primary_key=True, db_column='id')
	telefono = models.IntegerField( null = True, db_column='telefono' )
	direccion = models.CharField(max_length = 45, db_column='direccion')
	documento = models.IntegerField( db_column='documento')

	class Meta:
		db_table = 'usuarios'
		managed  = False

class Cliente(models.Model):
	id = models.OneToOneField(User, primary_key=True, db_column='id')
	telefono = models.IntegerField( null = True, db_column='telefono' )
	direccion = models.CharField(max_length = 145, db_column='direccion')
	documento = models.IntegerField( db_column='documento')

	class Meta:
		db_table = 'clientes'
		managed  = False

class Restaurante(models.Model):
	nombre = models.CharField(max_length = 45, db_column='nombre')
	telefono = models.CharField(max_length = 45, db_column='telefono')
	direccion = models.CharField(max_length = 45, db_column='direccion')
	sitioweb = models.CharField(max_length = 45, db_column='sitioweb')
	restaurante_cliente = models.ForeignKey(Cliente , db_column='restaurante_cliente')


	class Meta:
		db_table = 'restaurante'
		managed  = False

class Usuario_Restaurante(models.Model):
	usuario_restaurante_usuario = models.ForeignKey(Usuario, db_column='usuarios_restaurante_usuarios')
	usuario_restaurante_restaurante = models.ForeignKey(Restaurante , db_column='usuarios_restaurante_restaurante')

	class Meta:
		db_table = 'usuarios_restaurante'
		managed  = False

class Platillo(models.Model):
	nombre = models.CharField(max_length = 45, db_column='nombre')
	precio = models.IntegerField( db_column='precio')
	comentario = models.CharField(max_length = 100, db_column='comentario')
	restaurante_platillo = models.ForeignKey(Cliente , db_column='restaurante_platillo')


	class Meta:
		db_table = 'platillos'
		managed  = False