from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status


# Create your views here.

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print("*********List*********")
        print("basename",self.basename)
        print("Action",self.action)
        print("Detail",self.detail)
        print("Suffix",self.suffix)
        print("Name",self.name)
        print("Description",self.description)
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created.'},status = status.HTTP_201_CREATED)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id=pk
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data updated.'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        id = pk
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student,data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Updated.'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        id = pk
        student = Student.objects.get(id=id)
        student.delete()
        return Response({'msg':'Delete Data'})


