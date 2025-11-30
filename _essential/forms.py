from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
  username = forms.CharField(
    label = "Usuário", 
    max_length = 255
  )
  email = forms.EmailField(
    label = "E-mail", 
    help_text = "", 
    max_length = 255, 
    widget = forms.TextInput(
      attrs = { "placeholder": "ex.: nome@email.com" }
    )
  )
  first_name = forms.CharField(
    label = "Nome", 
    max_length = 255
  )
  last_name = forms.CharField(
    label = "Sobrenome", 
    max_length = 255
  )
  password = forms.CharField(
    label = "Senha", 
    widget = forms.PasswordInput, 
    min_length = 3
  )
  confirm = forms.CharField(
    label = "Confirme a senha", 
    widget = forms.PasswordInput, 
    help_text = "Reescreva igualmente a senha para confirmação"
  )
  
  def clean(self):
    cd = super().clean()
    if cd.get("password") != cd.get("confirm"):
      self.add_error("confirm", "Senha não confirma")
    elif User.objects.filter(username=cd.get("username")).first():
      self.add_error("username", "Usuário já cadastrado")
    return cd
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields:
      self.fields[field].widget.attrs['class'] = 'form-control'
      if not 'placeholder' in self.fields[field].widget.attrs:
        self.fields[field].widget.attrs['placeholder'] = self.fields[field].label

class SignInForm(forms.Form):
  username = forms.CharField(
    label = "Usuário", 
    max_length=255
  )
  password = forms.CharField(
    label = "Senha", 
    widget = forms.PasswordInput
  )
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields:
      self.fields[field].widget.attrs['class'] = 'form-control form-control-lg'
      if not 'placeholder' in self.fields[field].widget.attrs:
        self.fields[field].widget.attrs['placeholder'] = self.fields[field].label