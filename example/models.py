from django.db import models
from django.views.generic.base import ContextMixin
from django.conf import settings
import re


class MyContext(ContextMixin):
	def get_title(self):
		title = None
		sn = self.__class__.__name__
		sn = re.sub(r'List$', '', sn)
		sn = re.sub(r'Create$', '', sn)
		sn = re.sub(r'Update$', '', sn)
		sn = re.sub(r'Detail$', '', sn)
		sn = re.sub(r'Delete$', '', sn)
		bn = self.__class__.__bases__[1].__name__
		if   bn == "ListView":   title = "Listar " + sn
		elif bn == "CreateView": title = "Criar " + sn
		elif bn == "UpdateView": title = "Atualizar " + sn
		elif bn == "DetailView": title = "Visualizar " + sn
		elif bn == "DeleteView": title = "Excluir " + sn
		return title

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = self.get_title()
		context["sidenav"] = settings.SIDENAV
		context["is_authenticated"] = self.request.user.is_authenticated
		return context

class Pessoa(models.Model):
	nome = models.CharField(max_length = 255)
	email = models.EmailField()
	cpf = models.CharField(max_length = 19)

	def __str__(self):
		return self.nome

class Filho(models.Model):
	nome = models.CharField(max_length = 255)
	dta_nasc = models.DateField("data de nascimento")
	pessoa = models.ForeignKey(Pessoa, on_delete=models.RESTRICT)

	def __str__(self):
		return self.nome
