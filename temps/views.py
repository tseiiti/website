from django.shortcuts import render
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from temps.models import Temp
from temps.serializers import TempSerializer

from django.views.decorators.csrf import csrf_exempt
from spyne.server.django import DjangoApplication
from .services import soap_app

my_soap = csrf_exempt(DjangoApplication(soap_app))

params = { "sidenav": settings.SIDENAV }

def index(request):
  params["title"] = "Temperaturas"
  params["user"] = request.user
  tamanho = int(request.GET.get("tamanho") or "15")
  params["tamanho"] = tamanho
  total = Temp.objects.count()
  total = int(total / tamanho) + (total % tamanho > 0)
  page = int(request.GET.get("page") or "1")
  params["page"] = {
    '1': 1 if page > 1 else None,
    '2': page - 3 if page - 3 > 1 else None,
    '3': page - 2 if page - 2 > 1 else None,
    '4': page - 1 if page - 1 > 1 else None,
    '5': page,
    '6': page + 1 if page + 1 < total else None,
    '7': page + 2 if page + 2 < total else None,
    '8': page + 3 if page + 3 < total else None,
    '9': total if page < total else None,
  }
  return render(request, "temps/index.html", params)

@api_view()
def view_dtl(request):
  return Response({'success': 409, 'message': 'api'})

# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@api_view(['GET', 'POST'])
def view_temp(request):
  if request.method == 'GET':
    page = request.GET.get("page")
    if page:
      page     = int(page)
      tamanho  = int(request.GET.get("tamanho")) or 10
      temp_obj = Temp.objects.order_by("-id")[(page - 1) * tamanho:page * tamanho]
    else:
      temp_obj = Temp.objects.order_by("-id")
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
