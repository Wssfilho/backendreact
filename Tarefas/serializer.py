from rest_framework import serializers
from .models import Tarefa


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ('id', 'titulo', 'desc', 'data_vencimento', 'prioridade', 'status', 'vinculo')

