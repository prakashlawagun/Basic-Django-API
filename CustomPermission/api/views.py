from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import  IsAuthenticated


# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def StudentAuthentication(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        id = pk
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PATCH':
        id = pk
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partially updated.'})
        return Response(serializer.errors)

    if request.method == 'DEELTE':
        id = pk
        student = Student.objects.get(id=id)
        student.delete()
        return Response({'msg': 'Data Deleted'})
