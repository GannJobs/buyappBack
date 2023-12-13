from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Produto
from categorias.models import Categorias
from .serializer import ProdutosSerializer
from rest_framework.response import Response

# Create your views here.
class ProdutoModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProdutosSerializer
    queryset = Produto.objects.all()

    def create(self, request):
        categoria = request.data.get('Catid')
        Cat = Categorias.objects.get(id=categoria)
        nome = request.data.get('nome')
        valor = request.data.get('valor')
        marca = request.data.get('marca')
        img = request.data.get('img')
        Produto.objects.create(Nome=nome,Valor=valor,img=img,Marca=marca,Categoria=Cat)
        return Response({'status': 200, 'msg': 'created'})

    def delete(self, request):
        id = request.GET.get('id')
        prod = Produto.objects.get(id=id)
        print(id)
        prod.delete()
        return Response({'status': 200, 'msg': 'deleted Product'})