from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import UserForm

def index(request):
  now = datetime.now()
  html = f'''
  <html>
    <body>
      <h1>Hello from Vercel!</h1>
      <p>The current time is { now }.</p>
    </body>
  </html>
  '''
  return HttpResponse(html)

def home(request):
  is_authenticated = request.user.is_authenticated
  if is_authenticated:
    return render(request, "home.html", { "title": "Home", "sidenav": settings.SIDENAV, "is_authenticated": is_authenticated })
  else:
    return render(request, "home_external.html", { "title": "Home" })

def signup(request):
  if request.method == "GET":
    return render(request, "app/signup.html", { "form": UserForm })
  else:
    username = request.POST.get("username")
    email = request.POST.get("email")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    password = request.POST.get("password")
    confirm = request.POST.get("confirm")
    # return HttpResponse(dict(request))
    if password == "": 
      # form = UserForm(request.POST)
      # raise form.ValidationError("This error was added to show the non field errors styling.")
      return render(request, "app/signup.html", { "errors": [{ "field": "password", "message": "Senha inválida" }], "form": UserForm(request.POST) })
    if password != confirm:
      return render(request, "app/signup.html", { "errors": [{ "field": "confirm", "message": "Senha não confirma" }], "form": UserForm(request.POST) })
    if username == "":
      return render(request, "app/signup.html", { "errors": [{ "field": "username", "message": "Usuário inválido" }], "form": UserForm(request.POST) })
    user = User.objects.filter(username=username).first()
    if user:
      return render(request, "app/signup.html", { "errors": [{ "field": "username", "message": "Usuário já cadastrado" }], "form": UserForm(request.POST) })
    
    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    user = authenticate(username=username, password=password)
    login(request, user)
    reverse_lazy("modelo:list")

def signin(request):
  if request.method == "GET":
    return render(request, "app/signin.html")
  else:
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user:
      login(request, user)
      reverse_lazy("modelo:list")
    else:
      return render(request, "app/signin.html", { "errors": [{ "field": "username", "message": "Usuário/Senha inválido" }]})

@login_required(login_url="")
def signout(request):
  if request.method == "GET":
    return render(request, "app/signout.html")
  else:
    logout(request)
    return HttpResponse("Logout")