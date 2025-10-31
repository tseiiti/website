from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("signup", views.signup, name="signup"),
  path("accounts/login/", views.signin, name="signin"),
  path("accounts/logout/", views.signout, name="signout"),
]