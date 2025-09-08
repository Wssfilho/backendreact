from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Usuario


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'first_name']
        
class UsuarioSerializer(serializers.ModelSerializer):
    Vinculado = UserSerializer()

    class Meta:
        model = Usuario
        fields = '__all__'
