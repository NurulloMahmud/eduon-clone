from django.urls import path
from .views import RegisterAPIView, UserInfoAPIView, LogoutAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('user-info', UserInfoAPIView.as_view(), name='user_info'),
    path('logout', LogoutAPIView.as_view(), name='logout'),
]
