from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.EmailField('E-mail', max_length=70)
	cpf = models.CharField('CPF', max_length=11)
	celular = models.CharField('Celular', max_length=11)
	matricula = models.CharField('Matrícula', max_length=15)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.nome

class Areas(models.Model):
	nome = models.CharField('Nome', max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.nome


class Publicos(models.Model):
	nome = models.CharField('Nome', max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nome


class Cursos(models.Model):
	nome = models.CharField('Nome', max_length=150)
	resumo = models.TextField('Resumo', max_length=500)
	carga_horaria = models.IntegerField('Carga Horária', validators=[MinValueValidator(10), MaxValueValidator(160)])
	data_inicio = models.DateField('Data de Início')
	vagas = models.IntegerField('Vagas')
	foto = models.ImageField('Foto', upload_to='cursos')
	area = models.ForeignKey(Areas, on_delete=models.PROTECT)
	publicos = models.ManyToManyField(Publicos)
	autor = models.ForeignKey(User, related_name='autor', on_delete=models.PROTECT)
	inscritos = models.ManyToManyField(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nome