from .models import Loja
from rest_framework.serializers import ModelSerializer

class LojaSerializer(ModelSerializer):
    class Meta:
        model = Loja
        fields = '__all__'