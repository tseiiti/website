from django import forms
from django.views.generic.base import ContextMixin
from django.conf import settings
import re

from .models import Pessoa, Filho

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
		context["user"] = self.request.user
		return context

class PessoaForm(forms.ModelForm):
	class Meta:
		model = Pessoa
		fields = '__all__'
		
	email = forms.EmailField(label = "E-mail")
	cpf = forms.CharField(label = "CPF")

class FilhoForm(forms.ModelForm):
	class Meta:
		model = Filho
		fields = ('nome', 'dta_nasc')

	nome = forms.CharField(
		max_length = 255,
		widget = forms.TextInput(attrs = { "class": "form-control" })
	)
	dta_nasc = forms.DateField(
		label = "Data de nascimento", 
		widget = forms.DateInput(attrs = { "class": "form-control" })
	)

FilhoFormSet = forms.formset_factory(FilhoForm, extra=3)
