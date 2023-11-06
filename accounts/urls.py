from django.urls import path
from rest_framework.simplejwt.views import (# noqa
    TokenObtainPairView,# noqa
    TokenRefreshView, TokenBlacklistView, # noqa
)

from .views import RegisterAPIView, UserInfoAPIView, LogoutAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('user-info', UserInfoAPIView.as_view(), name='user_info'),
    path('logout', LogoutAPIView.as_view(), name='logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
