from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm

def index(request):
	is_authenticated = request.user.is_authenticated
	if is_authenticated:
		return render(request, "index.html", { "title": "Home", "sidenav": settings.SIDENAV, "is_authenticated": is_authenticated })
	else:
		return render(request, "index_external.html", { "title": "Home" })

def signup(request):
	if request.method == "GET":
		return render(request, "signup.html", { "form": UserForm })
	else:
		form = UserForm(request.POST)
		if form.is_valid():
			# messages.success(request, 'You have successfully updated the status from open to Close')
			user = User.objects.create_user(
				username = request.POST.get("username"),
				email = request.POST.get("email"),
				first_name = request.POST.get("first_name"),
				last_name = request.POST.get("last_name"),
				password = request.POST.get("password")
			)
			user = authenticate(
				username=request.POST.get("username"),
				password=request.POST.get("password")
			)
			login(request, user)
			return HttpResponseRedirect(reverse("example:list"))
		else:
			form.add_error(None, "Erro(s) foram encontrado(s) ao criar a conta. Favor fazer a devidas correções e tentar novamente.")
			return render(request, "signup.html", { "form": form})

def signin(request):
	if request.method == "GET":
		return render(request, "signin.html")
	else:
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			reverse_lazy("example:list")
		else:
			return render(request, "signin.html", { "errors": [{ "field": "username", "message": "Usuário/Senha inválido" }]})

@login_required(login_url="")
def signout(request):
	if request.method == "GET":
		return render(request, "signout.html")
	else:
		logout(request)
		return HttpResponse("Logout")