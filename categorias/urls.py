from rest_framework.routers import SimpleRouter
from .views import CategoraisModelViewSet

CatRouter = SimpleRouter()
CatRouter.register('Cat', CategoraisModelViewSet)