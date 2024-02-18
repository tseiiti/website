# from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import MyContext, Pessoa

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
