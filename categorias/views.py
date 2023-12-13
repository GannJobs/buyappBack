from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Categorias
from user.models import Usuario
from loja.models import Loja
from produtos.models import Produto
from produtos.serializer import ProdutosSerializer
from .serializer import CategoriasSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class CategoraisModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = CategoriasSerializer
    queryset = Categorias.objects.all()

    def list(self, request):  
        dono = Usuario.objects.get(Pessoa=request.user)
        loja = Loja.objects.get(Dono=dono)
        categorias = Categorias.objects.filter(Loja=loja)

        categorias_data = []
        for categoria in categorias:
            produtos = Produto.objects.filter(Categoria=categoria)
            produtos_serializer = ProdutosSerializer(produtos, many=True)
            categoria_data = {
                'id': categoria.id,
                'nome': categoria.Nome,
                'descricao': categoria.Descricao,
                'produtos': produtos_serializer.data,
            }
            categorias_data.append(categoria_data)
        return Response({'status': 200, 'Categorias': categorias_data})
   
    @action(methods=["get"], detail=False)
    def espec(self, request):  
        id = request.data.get('id')
        loja = Loja.objects.get(id=id)
        categorias = Categorias.objects.filter(Loja=loja)
        serializer = CategoriasSerializer(categorias, many=True)
        return Response({'status': 200, 'Categorias': serializer.data})

    def create(self, request):
        nome = request.data.get('nome')
        descricao = request.data.get('descricao')
        loja = request.data.get('lojaId')
        Lj = Loja.objects.get(id=loja)
        Categorias.objects.create(Nome=nome, Descricao=descricao, Loja=Lj)
        return Response({'status': 200, 'msg': 'created'})

    def delete(self, request):
        id = request.GET.get('id')
        categoria = Categorias.objects.get(id=id)
        produtos = Produto.objects.filter(Categoria=categoria)
        for obj in produtos:
            obj.delete()
        categoria.delete()
        return Response({
            'status': 200,
            'Categorias': 'Categorai Excluded'
        })