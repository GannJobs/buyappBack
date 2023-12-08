from .models import Usuario, User
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']

class UsuarioSerializer(ModelSerializer):
    Pessoa = UserSerializer()

    class Meta:
        model = Usuario
        fields = '__all__'

class LogoutSerializer(ModelSerializer):
    class Meta:
        model = User
        fields= []