from django.db import models

class Temp(models.Model):
  ip = models.CharField(max_length=15)
  pai = models.CharField(max_length=17)
  endereco = models.CharField(max_length=17)
  temperatura = models.DecimalField(max_digits=5, decimal_places=2)
  data_hora = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.endereco