from .views import CategoraisModelViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'Catg', CategoraisModelViewSet, basename='Catg')

urlpatterns = [
    path('', include(router.urls)),
]