# from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.db import transaction

from .models import Pessoa
from .forms import PessoaForm, FilhoFormSet

class CreatePessoaView(CreateView):
	template_name = 'example/create_pessoa.html'
	model = Pessoa
	form_class = PessoaForm
	success_url = './'

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	if self.request.POST:
	# 		context['formset'] = FilhoFormSet(self.request.POST, self.request.FILES, instance=self.object)
	# 	else:
	# 		context['formset'] = FilhoFormSet(instance=self.object)
	# 	return context
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['formset'] = FilhoFormSet(initial=self.object)
		return context
	

# formset = FilhoFormSet(
#   initial = [
#     { "nome": "teste", "dta_nasc": datetime.date.today() }
# 	]
# )

	def form_valid(self, form, formset):
		with transaction.atomic():
			self.object = form.save()

		if formset.is_valid():
			formset.instance = self.object
			formset.save()

		return super().form_valid(form)

	def post(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		formset = FilhoFormSet(self.request.POST, self.request.FILES)
		if form.is_valid() and formset.is_valid():
			return self.form_valid(form, formset)
		else:
			return self.form_invalid(form, formset)

	def form_invalid(self, form, formset):
		return self.render_to_response(self.get_context_data(form=form, formset=formset))




class PessoaList(ListView):
	model = Pessoa
	queryset = Pessoa.objects.all()

class PessoaCreate(CreateView):
	model = Pessoa
	fields = "__all__"
	success_url = reverse_lazy("example:list")

class PessoaUpdate(UpdateView):
	model = Pessoa
	fields = "__all__"
	success_url = reverse_lazy("example:list")

class PessoaDetail(DetailView):
	queryset = Pessoa.objects.all()

class PessoaDelete(DeleteView):
	queryset = Pessoa.objects.all()
	success_url = reverse_lazy("example:list")
