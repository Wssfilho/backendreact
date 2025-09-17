# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Tarefa
from .serializer import TarefaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication   
from rest_framework.decorators import action
from rest_framework.response import Response
from Usuario.models import Usuario



class TarefaModelViewSet(ModelViewSet):
    # authenticacao
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = TarefaSerializer
    queryset = Tarefa.objects.all()
    
    def list(self, request):
        taf = Tarefa.objects.all()
        serial = TarefaSerializer(taf, many = True)
        if len(serial.data) > 0:
            return Response({'status': 302, 'Tarefa':
                serial.data})
        return Response({'status': 204, 'msg': 'No content'})
    
    def create(self, request):
        vinculo = Usuario.objects.get(Vinculado=request.user)
        titulo = request.data.get('titulo')
        desc = request.data.get('descricao')
        data = request.data.get('data_vencimento')
        prioridade = request.data.get('prioridade')
        status = request.data.get('status')
        Tarefa.objects.create(vinculo = vinculo, titulo = titulo, 
                              desc = desc, data_vencimento = data,
                              prioridade = prioridade, status = status
                              )
        return Response({'status': 201, 'msg': 'registered successfully'})
    
    # retornar as tarefas por prioridade
    @action(methods=["get"], detail=False)
    def TafOrder(self, request):
        # crescente, decrescente '-prioridade'
        Us = Usuario.objects.get(Vinculado=request.user)
        taf = Tarefa.objects.filter(vinculo=Us).order_by('-prioridade')
        serial = TarefaSerializer(taf, many=True)
        if len(serial.data) > 0:
            return Response({
                'status': 302, 'Lista de Prioridade': serial.data
            })
        return Response({'status': 204, 'msg': 'No Content'})
    
    
    def patch(self, request):
        id = request.data.get('id')
        taf = Tarefa.objects.get(id=id)
        titulo = request.data.get('titulo')
        desc = request.data.get('descricao')
        data = request.data.get('data_vencimento')
        p = request.data.get('prioridade')
        status = request.data.get('status')
        taf.titulo = titulo
        taf.desc = desc
        taf.data_vencimento = data
        taf.prioridade = p
        taf.status = status
        taf.save()
        return Response({'status': 200, 'msg': 'Updated!'})
        
    def delete(self, request):
        id = request.GET.get('id')
        if not id:
            return Response({'status':404, 'msg': 'bad request', 'id': id})
        taf = Tarefa.objects.filter(id=id)
        taf.delete()
        return Response({'status': 200, 'msg': 'Deleted!'})
        
        
        