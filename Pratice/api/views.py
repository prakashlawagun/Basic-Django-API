from django.shortcuts import render
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse


# Create your views here.
def student_detial(request):
    stu = Student.objects.get(id=1)
    serializer = StudentSerializer(stu)
    return JsonResponse(serializer.data)


def student_list(request):
    stu = Student.objects.all()
    serializers = StudentSerializer(stu,many=True)
    return JsonResponse(serializers.data,safe=  False)
