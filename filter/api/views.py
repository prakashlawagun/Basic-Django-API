from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView


# Create your views here.
class StudentAPImodel(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','city']


