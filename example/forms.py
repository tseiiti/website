from django import forms
# from django.forms import ModelForm, inlineformset_factory, formset_factory
from .models import Pessoa, Filho

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
		context["user"] = self.request.user
		return context

class PessoaForm(ContextMixin, forms.ModelForm):
  class Meta:
    model = Pessoa
    fields = '__all__'

class FilhoForm(ContextMixin, forms.ModelForm):
  class Meta:
    model = Filho
    # fields = '__all__'
    fields = ('nome', 'dta_nasc')

# FilhoFormSet = inlineformset_factory(Pessoa, Filho, fields='__all__')
FilhoFormSet = forms.formset_factory(FilhoForm, extra=3)

# formset = FilhoFormSet(
#   initial = [
#     { "nome": "teste", "dta_nasc": datetime.date.today() }
# 	]
# )



# (
#   parent_model: type[Model], 
#   model: type[Model], 
#   form: type[ModelForm] = ..., 
#   formset: type[BaseInlineFormSet] = ..., 
#   fk_name: str | None = ..., 
#   fields: _Fields | None = ..., 
#   exclude: _Fields | None = ..., 
#   extra: int = ..., 
#   can_order: bool = ..., 
#   can_delete: bool = ..., 
#   max_num: int | None = ..., 
#   formfield_callback: ((...) -> Any) | None = ..., 
#   widgets: dict[str, Any] | None = ..., 
#   validate_max: bool = ..., 
#   localized_fields: Sequence[str] | None = ..., 
#   labels: dict[str, str] | None = ..., 
#   help_texts: dict[str, str] | None = ..., 
#   error_messages: dict[str, dict[str, str]] | None = ..., 
#   min_num: int | None = ..., 
#   validate_min: bool = ..., 
#   field_classes: dict[str, Any] | None = ...
# ) -> type[BaseInlineFormSet]