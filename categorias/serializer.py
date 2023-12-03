from .models import Categorias
from produtos.serializer import ProdutosSerializer
from rest_framework.serializers import ModelSerializer

class CategoriasSerializer(ModelSerializer):
    produtos = ProdutosSerializer(many=True, read_only=True)

    class Meta:
        model = Categorias
        fields = ['Nome','Descricao','Loja','produtos']