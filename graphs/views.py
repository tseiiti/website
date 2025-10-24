from django.shortcuts import render
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Temp
from .serializers import TempSerializer

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




def temps(request):
  params["title"] = "Temps"
  params["user"] = request.user
  params["object_list"] = Temp.objects.order_by("-id")[:20]
  return render(request, "graphs/temps.html", params)

@api_view()
def view_dtl(request):
  return Response({'success': 409, 'message': 'api'})

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def view_temp(request):
  if request.method == 'GET':
    temp_obj = Temp.objects.all()
    serializer = TempSerializer(temp_obj, many=True)
    return Response({'msg': 'Successfully retrieved data', 'data': serializer.data}, status=status.HTTP_200_OK)

  elif request.method == 'POST':
    serializer = TempSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg': 'Temp created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'PUT':
    temp_obj = Temp.objects.get(pk=request.data.get('id'))
    serializer = TempSerializer(temp_obj, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg': 'Temp updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'PATCH':
    temp_obj = Temp.objects.get(pk=request.data.get('id'))
    serializer = TempSerializer(temp_obj, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg': 'Temp updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    temp_obj = Temp.objects.get(pk=request.data.get('id'))
    temp_obj.delete()
    return Response({'msg': 'Temp deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

  return Response({'msg': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
