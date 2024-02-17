from django.db import models

class Pessoa(models.Model):
  nome = models.CharField(max_length = 255)
  email = models.EmailField()
  cpf = models.CharField(max_length = 19)

  def __str__(self):
    return self.nome

class Filho(models.Model):
  nome = models.CharField(max_length = 255)
  dta_nasc = models.DateField("data de nascimento")
  pessoa = models.ForeignKey(Pessoa, on_delete=models.RESTRICT)

  def __str__(self):
    return self.nome
