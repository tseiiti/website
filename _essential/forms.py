from django import forms

class UserForm(forms.Form):
  username = forms.CharField(label="Usuário", max_length=255)
  email = forms.EmailField(label="E-mail", help_text="", max_length=255, widget=forms.TextInput(attrs={ "placeholder": "ex.: name@example.com" }))
  first_name = forms.CharField(label="Nome", max_length=255)
  last_name = forms.CharField(label="Sobrenome", max_length=255)
  password = forms.CharField(label="Senha", widget=forms.PasswordInput)
  confirm = forms.CharField(label="Confirme a senha", widget=forms.PasswordInput, help_text="<i>Reescreva igualmente a senha para confirmação</i>")

  # def clean(self):
  #   cleaned_data = super().clean()
  #   raise forms.ValidationError("This error was added to show the non field errors styling.")
  #   return cleaned_data
  
  # def clean(self):
  #     cleaned_data = super().clean()
  #     cc_myself = cleaned_data.get("cc_myself")
  #     subject = cleaned_data.get("subject")

  #     if cc_myself and subject:
  #         # Only do something if both fields are valid so far.
  #         if "help" not in subject:
  #             raise ValidationError(
  #                 "Did not send for 'help' in the subject despite "
  #                 "CC'ing yourself."
  #             )