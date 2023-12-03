from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Usuario
from .serializer import UsuarioSerializer, LogoutSerializer
from rest_framework.decorators import action
from django.contrib.auth import logout
from rest_framework.response import Response

# Create your views here.
class UsuarioModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

# retornar os dados principais
    @action(methods=["get"], detail=False)
    def me(self, request):
        user = Usuario.objects.get(Ente=request.user)
        serial = UsuarioSerializer(user)
        return Response({'status': 302, 'Entidade': serial.data})
    
class LogoutModelView(ModelViewSet):
    serializer_class = LogoutSerializer
    queryset = Usuario.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def create(self, request):
        self.request.user.auth_token.delete()
        logout(self.request)
        return Response({"msg": 'User Logged out successfully'})
