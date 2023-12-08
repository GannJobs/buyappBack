from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Loja
from user.models import Usuario
from .serializer import LojaSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


# Create your views here.
class LojaModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = LojaSerializer
    queryset = Loja.objects.all()

    def list(self, request):
        dono = Usuario.objects.get(Pessoa=request.user)
        l = Loja.objects.get(Dono=dono)
        loja = LojaSerializer(l)    
        return Response({
            'status':302,
            'Loja': loja.data
        })
    
    @action(methods=["get"], detail=False)
    def lojaU(self, request):
        id = request.GET.get('id')
        l = Loja.objects.get(id=id)
        loja = LojaSerializer(l)    
        return Response({
            'status':302,
            'Loja': loja.data
        })