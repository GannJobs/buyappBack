from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Loja
from user.models import Usuario
from .serializer import LojaSerializer
from rest_framework.response import Response

# Create your views here.
class LojaModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = LojaSerializer
    queryset = Loja.objects.all()

    def list(self, request):
        dono = Usuario.objects.get(Ente=request.user)
        l = Loja.objects.get(Dono=dono)
        loja = LojaSerializer(Loja)    
        return Response({
            'status':200,
            'Loja': loja.data
        })