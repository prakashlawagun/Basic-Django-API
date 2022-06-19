
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stdapi/',views.StudentList.as_view()),
    # path('stdapi/',views.StudentCreate.as_view())
    # path('stdapi/<int:pk>/',views.StudentRetrieve.as_view()),
    # path('stdapi/<int:pk>/',views.StudentUpdate.as_view()),
    # path('stdapi/<int:pk>/',views.StudentDelete.as_view()),
    path('stdapi/',views.ListCreate.as_view()),
    path('stdapi/<int:pk>/',views.RUDStudent.as_view()),
]
