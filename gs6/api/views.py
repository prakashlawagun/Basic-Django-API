from django.shortcuts import render

from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.

class StudentAPI(APIView):
    def get(self, request, pk=None,format=None):
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data complete updated.'})
        return Response(serializer.errors)

    def patch(self, request, pk,format=None):
        id = pk
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data partial  updated.'})
        return Response(serializer.errors)

    def delete(self, request, pk,format=None):
        id = pk
        student = Student.objects.get(id=id)
        student.delete()
        return Response({'msg': 'Data Deleted.'})
