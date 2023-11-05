from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import (
    UserSerializer,
    SubCategorySerializer,
    MainCategorySerializer,
)


User = get_user_model()

