from rest_framework.routers import DefaultRouter
from .views import UsuarioModelViewSet, LogoutModelView
from django.urls import path, include

router = DefaultRouter()
router.register(r'user', UsuarioModelViewSet, basename='user')
router.register(r'logout', LogoutModelView, basename='logout')

urlpatterns = [
    path('', include(router.urls)),
]