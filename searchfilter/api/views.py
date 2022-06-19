from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListAPIView


# Create your views here.
class StudentAPImodel(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filter_backends = [SearchFilter]
    # search_fields = ['city',]

    filter_backends = [OrderingFilter]
    ordering_fields =['name']



