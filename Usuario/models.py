from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Usuario(models.Model):
    Vinculado = models.ForeignKey(User, on_delete=models.CASCADE)
    Telefone = models.CharField(max_length=11, default='00000000000')
    CPF = models.CharField(max_length=11, default='11111111111')
    
    def __str__(self):
        return self.Vinculado.username