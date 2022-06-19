from rest_framework.routers import DefaultRouter
from .views import AddressViewSet
from django.urls import path,include
router = DefaultRouter()
router.register('/address',AddressViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
]