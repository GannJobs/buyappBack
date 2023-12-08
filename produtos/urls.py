from .views import ProdutoModelViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'prod', ProdutoModelViewSet, basename='prod')

urlpatterns = [
    path('', include(router.urls)),
]