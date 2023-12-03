from rest_framework.routers import SimpleRouter
from .views import ProdutoModelViewSet

ProdRouter = SimpleRouter()
ProdRouter.register('Prod', ProdutoModelViewSet)