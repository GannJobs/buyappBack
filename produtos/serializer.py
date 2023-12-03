from .models import Produto
from rest_framework.serializers import ModelSerializer

class ProdutosSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'