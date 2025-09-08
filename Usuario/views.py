# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Usuario
from .serializer import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication   
from rest_framework.decorators import action
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth.models import User


class UsuarioModelViewSet(ModelViewSet):
    # authenticacao
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

    # Listar usuarios
    def list(self, request):
        usuario = Usuario.objects.all()
        serial = UsuarioSerializer(usuario, many=True)
        if len(serial.data) > 0:
            return Response({
                'status': 302, 'Usuario': serial.data
            })
        return Response({'status': 204, 'msg': 'No Content'})

    # retornar os dados do usuário
    @action(methods=["get"], detail=False)
    def me(self, request):
        usuario = Usuario.objects.get(Vinculado=request.user)
        serial = UsuarioSerializer(usuario)
        return Response({'status': 302, 'Usuario': serial.data})

    # criar um usuário
    def create(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        hashed_password = make_password(password)
        user_exists = User.objects.filter(username=username).exists()
        if user_exists:
            response_data = {'status': 409,
                             'errorType': 'NameError', 'errorAt': 'username'}
            return JsonResponse(response_data, status=409)
        else:
            name = request.data.get('first name')
            email = request.data.get('email')
            tel = request.data.get('telefone')
            cpf = request.data.get('cpf')
            usuario = User.objects.create(
                username=username, password=hashed_password, email=email, first_name=name, last_name=" ")
            user = Usuario.objects.create(
                Vinculado=usuario, Telefone=tel, cpf=cpf)
            usuario.save()
            user.save()
            return Response({'status': 201, 'msg': 'registered successfully'})

    # att um usuarioo
    def patch(self, request):
        obj = Usuario.objects.get(Vinculado=request.user)
        name = request.data.get('first name')
        email = request.data.get('email')
        tel = request.data.get('telefone')
        cpf = request.data.get('cpf')
        obj.Vinculado.first_name = name
        obj.Vinculado.email = email
        obj.Telefone = tel
        obj.cpf = cpf
        obj.Vinculado.save()
        obj.save()
        return Response({'status': 200, 'msg': 'OK'})

    def delete(self, request):
        id = request.GET.get('id')
        obj = Usuario.objects.get(id=id)
        obj.Vinculado.delete()
        obj.delete()
        return Response({'status': 200, 'msg': 'Deleted'})