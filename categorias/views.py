from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Categorias
from user.models import Usuario
from loja.models import Loja
from produtos.models import Produto
from .serializer import CategoriasSerializer
from rest_framework.response import Response

# Create your views here.
class CategoraisModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = CategoriasSerializer
    queryset = Categorias.objects.all()

    def list(self, request):  
        dono = Usuario.objects.get(Ente=request.user)
        loja = Loja.objects.get(Dono=dono)
        categoria = Categorias.objects.filter(Loja=loja, many=True)
        data = CategoriasSerializer(categoria, many=True)
        return Response({
            'status': 200,
            'Categorias': data.data
        })
    
    def create(self, request):
        nome = request.data.get('nome')
        descricao = request.data.get('descricao')
        loja = request.data.get('loja')
        Lj = Loja.objects.get(id=loja)
        Categorias.objects.create(Nome=nome, Descricao=descricao, Loja=Lj)
        return Response({'status': 200, 'msg': 'created'})

    def delete(self, request, id):
        categoria = Categorias.objects.get(id=id)
        produtos = Produto.objects.filter(Categoria=categoria)
        for obj in produtos:
            obj.delete()
        categoria.delete()
        return Response({
            'status': 200,
            'Categorias': 'Categorai Excluded'
        })