from django import forms
from .models import Pessoa

class PessoaForm(forms.Form):
  class Meta:
    model = Pessoa
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields:
      self.fields[field].widget.attrs['class'] = 'form-control'
      if not 'placeholder' in self.fields[field].widget.attrs:
        self.fields[field].widget.attrs['placeholder'] = self.fields[field].label