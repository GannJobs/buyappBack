from rest_framework.routers import SimpleRouter
from .views import UsuarioModelViewSet, LogoutModelView

UserRouter = SimpleRouter()
UserRouter.register('User', UsuarioModelViewSet)

LogoutUserRouter=SimpleRouter()
LogoutUserRouter.register('logout',LogoutModelView)