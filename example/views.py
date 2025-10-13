from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import MyContext, Pessoa
from django.conf import settings
from django.shortcuts import render

import io
import base64
import matplotlib.pyplot as plt
import seaborn as sns

params = { "sidenav": settings.SIDENAV }
def dashboard(request):
  params["title"] = "Dashboard"
  params["user"] = request.user
  return render(request, "example/dashboard.html", params)

def graf01(request):
  data = sns.load_dataset("iris")
  plt.figure(figsize=(8, 6))
  sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=data)
  plt.title("Iris Sepal Length vs. Width")

  buffer = io.BytesIO()
  plt.savefig(buffer, format='png')
  buffer.seek(0)
  plt.close()

  image_png = buffer.getvalue()
  graph = base64.b64encode(image_png)
  graph = graph.decode('utf-8')

  params["title"] = "Gráfico 01"
  params["user"] = request.user
  params["graph"] = graph

  return render(request, "example/graf01.html", params)

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
