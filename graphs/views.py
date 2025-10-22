from django.shortcuts import render
from django.conf import settings

import io
import base64
import matplotlib.pyplot as plt
import seaborn as sns

from pymongo.mongo_client import MongoClient
uri = settings.DATABASES['mongo']['URI']
client = MongoClient(uri)
dba = client['db_teste']

params = { "sidenav": settings.SIDENAV }
def powerbi(request):
  params["title"] = "Power BI"
  params["user"] = request.user
  return render(request, "graphs/powerbi.html", params)

def graph_01(request):
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

  return render(request, "graphs/graph_01.html", params)

def graph_02(request):
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

  return render(request, "graphs/graph_01.html", params)