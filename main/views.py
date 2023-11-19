from django.shortcuts import render

Create your views here.from rest_framework import generics
from .models import Kurs
from .serializers import KursSerializer
from .permissions import IsMentorPermission, HasBoughtCoursePermission

class KursDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
