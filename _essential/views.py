from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from _essential.forms import SignUpForm, SignInForm

def index(request):
	is_authenticated = request.user.is_authenticated
	if is_authenticated:
		return render(request, "index.html", { "title": "Home", "sidenav": settings.SIDENAV, "user": request.user })
	else:
		return render(request, "index_external.html", { "title": "Home" })

def signup(request):
	if request.method == "GET":
		return render(request, "signup.html", { "form": SignUpForm })
	else:
		post = request.POST
		form = SignUpForm(post)
		if form.is_valid():
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
			return redirect("index")
		else:
			for k in form.errors.keys():
				form.fields[k].widget.attrs['class'] += ' is-invalid'
			form.add_error(None, "Erro(s) foram encontrado(s) ao criar a conta. Favor fazer a devidas correções e tentar novamente.")
			return render(request, "signup.html", { "form": form })

def signin(request):
	if request.method == "GET":
		return render(request, "signin.html", { "form": SignInForm, "next": request.GET.get("next") })
	else:
		post = request.POST
		form = SignInForm(post)
		username = post.get("username")
		password = post.get("password")
		next = post.get("next")
		user = authenticate(username=username, password=password)
		if form.is_valid() and user:
			login(request, user)
			if next != "None":
				return redirect(next)
			else:
				return redirect("index")
		else:
			form.add_error("password", "")
			form.add_error("username", "")
			for k in form.errors.keys():
				form.fields[k].widget.attrs['class'] += ' is-invalid'
			form.add_error(None, "Usuário / Senha inválido")
			return render(request, "signin.html", { "form": form })

def signout(request):
	logout(request)
	return redirect("index")