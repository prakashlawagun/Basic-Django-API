from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('stdapi',views.StudentViewSet,basename='student')
# router.register('stdapi/<int:pk>',views.StudentViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
