from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm, SignInForm

def index(request):
	is_authenticated = request.user.is_authenticated
	if is_authenticated:
		return render(request, "index.html", { "title": "Home", "sidenav": settings.SIDENAV, "is_authenticated": is_authenticated })
	else:
		return render(request, "index_external.html", { "title": "Home" })

def signup(request):
	if request.method == "GET":
		return render(request, "signup.html", { "form": SignUpForm })
	else:
		post = request.POST
		form = SignUpForm(post)
		if form.is_valid():
			# messages.success(request, 'You have successfully updated the status from open to Close')
			user = User.objects.create_user(
				username = post.get("username"),
				email = post.get("email"),
				first_name = post.get("first_name"),
				last_name = post.get("last_name"),
				password = post.get("password")
			)
			user = authenticate(
				username=post.get("username"),
				password=post.get("password")
			)
			login(request, user)
			return HttpResponseRedirect(reverse("example:list"))
		else:
			form.add_error(None, "Erro(s) foram encontrado(s) ao criar a conta. Favor fazer a devidas correções e tentar novamente.")
			return render(request, "signup.html", { "form": form })

def signin(request):
	if request.method == "GET":
		return render(request, "signin.html", { "form": SignInForm })
	else:
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect(reverse("example:list"))
		else:
			post = request.POST
			form = SignInForm(post)
			form.add_error(None, "Usuário / Senha inválido")
			form.add_error("password", "")
			form.add_error("username", "")
			return render(request, "signin.html", { "form": form })

def signout(request):
	logout(request)
	return HttpResponseRedirect(reverse("index"))