from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from example.models import MyContext, Pessoa

class PessoaList(MyContext, ListView):
	model = Pessoa
	queryset = Pessoa.objects.all()

class PessoaCreate(MyContext, CreateView):
	model = Pessoa
	fields = "__all__"

class PessoaUpdate(MyContext, UpdateView):
	model = Pessoa
	fields = "__all__"

class PessoaDetail(MyContext, DetailView):
	queryset = Pessoa.objects.all()

class PessoaDelete(MyContext, DeleteView):
	queryset = Pessoa.objects.all()
