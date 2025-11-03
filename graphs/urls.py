from django.urls import path
from graphs.views import *

app_name = "graphs"
urlpatterns = [
  path("powerbi", powerbi, name="powerbi"), 
  path("graph_01", graph_01, name="graph_01"), 
  path("graph_02", graph_02, name="graph_02"), 
  path("graph_03", graph_03, name="graph_03"), 
  path("graph_04", graph_04, name="graph_04"), 
]
