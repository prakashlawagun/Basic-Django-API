from django.shortcuts import render
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework import viewsets


# Create your views here.

class StudentAuthentication(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
