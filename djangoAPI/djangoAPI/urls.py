
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('std/<int:pk>',views.student_detail,name="std"),
    path('stdinfo/',views.student_list,name="stdinfo"),
]
