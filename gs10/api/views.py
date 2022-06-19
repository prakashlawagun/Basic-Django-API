from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets


# Create your views here.
# class StudentViewAPI(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
class StudentReadOnlyViewAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
