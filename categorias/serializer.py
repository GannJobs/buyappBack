from .models import Categorias
from produtos.serializer import ProdutosSerializer
from rest_framework.serializers import ModelSerializer

class CategoriasSerializer(ModelSerializer):
    Produtos = ProdutosSerializer(many=True, read_only=True)

    class Meta:
        model = Categorias
        #fields = '__all__'
        fields = ['Nome','Descricao','Loja','Produtos']