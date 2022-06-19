from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .customauth import CustomAuthentications


# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomAuthentications]
    permission_classes = [IsAuthenticated]
