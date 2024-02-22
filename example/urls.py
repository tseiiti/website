from django.urls import path
from .views import PessoaList, PessoaCreate, PessoaUpdate, PessoaDetail, PessoaDelete, CreatePessoaView

app_name = "example"
urlpatterns = [
  path("list/",            PessoaList.as_view(),   name="list"),
  path("create/",          PessoaCreate.as_view(), name="create"),
  path("update/<int:pk>/", PessoaUpdate.as_view(), name="update"),
  path("detail/<int:pk>/", PessoaDetail.as_view(), name="detail"),
  path("delete/<int:pk>/", PessoaDelete.as_view(), name="delete"),
  path('create_pessoa/', CreatePessoaView.as_view(), name='create_pessoa'),
]
