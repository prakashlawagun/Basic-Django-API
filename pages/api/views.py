from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from .mypagination import MyPageNumberPagination
from rest_framework.generics import ListAPIView


# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination
