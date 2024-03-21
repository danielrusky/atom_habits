from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + router.urls