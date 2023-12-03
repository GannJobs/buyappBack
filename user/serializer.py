from .models import Usuario, User
from rest_framework.serializers import ModelSerializer

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class LogoutSerializer(ModelSerializer):
    class Meta:
        model = User
        fields= []