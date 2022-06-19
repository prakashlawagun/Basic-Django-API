from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from .mypaginations import MyLimitPageNumberPagination
from rest_framework.generics import ListAPIView


# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyLimitPageNumberPagination
