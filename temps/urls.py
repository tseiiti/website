from django.urls import path
from temps.views import *

app_name = "temps"
urlpatterns = [
  path("temps", temps, name="temps"), 
  path('temp', view_temp, name='temp'),
]
