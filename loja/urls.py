from rest_framework.routers import SimpleRouter
from .views import LojaModelViewSet

LojaRouter = SimpleRouter()
LojaRouter.register('Loja', LojaModelViewSet)