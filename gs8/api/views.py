from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer


# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RUDStudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
