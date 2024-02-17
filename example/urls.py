from django.urls import path
from . import views

app_name = "example"
urlpatterns = [
  path("list/",            views.PessoaList.as_view(),   name="list"),
  path("create/",          views.PessoaCreate.as_view(), name="create"),
  path("update/<int:pk>/", views.PessoaUpdate.as_view(), name="update"),
  path("detail/<int:pk>/", views.PessoaDetail.as_view(), name="detail"),
  path("delete/<int:pk>/", views.PessoaDelete.as_view(), name="delete"),
]
