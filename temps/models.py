from django.db import models

class Temp(models.Model):
  nome = models.CharField(max_length=15, null=True)
  ip = models.CharField(max_length=15)
  camada = models.IntegerField(null=True)
  pai = models.CharField(max_length=17)
  endereco = models.CharField(max_length=17)
  temperatura = models.DecimalField(max_digits=5, decimal_places=2)
  peso = models.DecimalField(max_digits=5, decimal_places=2, null=True)
  memoria = models.IntegerField(null=True)
  data_hora = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.endereco