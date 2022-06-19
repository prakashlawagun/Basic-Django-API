from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Address
from .serializers import AddressSerializer


# Create your views here.
class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
