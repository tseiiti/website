from django.db import models

class Temp(models.Model):
  mac_address = models.CharField(max_length=17)
  temperatura = models.DecimalField(max_digits=5, decimal_places=2)
  data_hora = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.mac_address