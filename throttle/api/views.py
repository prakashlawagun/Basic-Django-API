from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from  rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .throttling import JackRateThrottle


# Create your views here.
class StudentModelView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # throttle_classes = [AnonRateThrottle, JackRateThrottle]
