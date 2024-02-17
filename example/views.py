# from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.views.generic.base import ContextMixin
from django.urls import reverse_lazy
from django.conf import settings
from .models import Pessoa

class MyContext(ContextMixin):
  def get_title(self):
    title = None
    class_name = self.__class__.__name__
    if class_name == "PessoaList": title = "Listar Pessoas"
    elif class_name == "PessoaCreate": title = "Criar Pessoa"
    elif class_name == "PessoaUpdate": title = "Atualizar Pessoa"
    elif class_name == "PessoaDetail": title = "Visualizar Pessoa"
    elif class_name == "PessoaDelete": title = "Excluir Pessoa"
    return title

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["title"] = self.get_title()
    context["sidenav"] = settings.SIDENAV
    return context

class PessoaList(MyContext, ListView):
  model = Pessoa
  queryset = Pessoa.objects.all()

class PessoaCreate(MyContext, CreateView):
  model = Pessoa
  fields = "__all__"
  success_url = reverse_lazy("example:list")

class PessoaUpdate(MyContext, UpdateView):
  model = Pessoa
  fields = "__all__"
  success_url = reverse_lazy("example:list")

class PessoaDetail(MyContext, DetailView):
  queryset = Pessoa.objects.all()

class PessoaDelete(MyContext, DeleteView):
  queryset = Pessoa.objects.all()
  success_url = reverse_lazy("example:list")
