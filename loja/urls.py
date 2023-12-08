from .views import LojaModelViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'loja', LojaModelViewSet, basename='loja')

urlpatterns = [
    path('', include(router.urls)),
]