from django.db import models
from Usuario.models import Usuario
# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=20, default='Vazio')
    desc = models.CharField(max_length=100, default='Sem conteúdo')
    data_vencimento = models.DateField()
    prioridade = models.IntegerField(default=0)
    status = models.IntegerField(default=1) # 1 - Em Andamento, 2 - Concluido
    vinculo = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo