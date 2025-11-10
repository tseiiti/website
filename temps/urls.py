from django.urls import path
from temps.views import *

app_name = "temps"
urlpatterns = [
  path("", index, name="index"), 
  path('temp', view_temp, name='temp'),
  path("my_soap", my_soap, name="my_soap"), 
]
