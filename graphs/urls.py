from django.urls import path
from .views import *

app_name = "graphs"
urlpatterns = [
  path("powerbi", powerbi, name="powerbi"), 
  path("graph_01", graph_01, name="graph_01"), 
  path("graph_02", graph_02, name="graph_02"), 
  path("temps", temps, name="temps"), 
  path('temp', view_temp, name='temp'),
]
