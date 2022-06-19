from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stdapi/',views.StudentAuthentication,name="stdapi"),
    path('stdapi/<int:pk>',views.StudentAuthentication,name="stdapi"),

]
