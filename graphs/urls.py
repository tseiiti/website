from django.urls import path
from . import views

app_name = "graphs"
urlpatterns = [
  path("powerbi", views.powerbi, name="powerbi"), 
  path("graph_01", views.graph_01, name="graph_01"), 
  path("graph_02", views.graph_02, name="graph_02"), 
]
