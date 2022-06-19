from django.urls import path
from .views import *
app_name ='control'
urlpatterns = [
    path('',index,name='index'),
    path('add',addEmployee,name='addemp'),
    path('delete/<int:id>/',deleteEmployee,name='deleteemp'),
    path('view/<int:id>/',viewEmployee,name='viewemp'),
    path('edit/<int:id>',editEmployee,name='editemp'),
    path('search',searchEmployee,name='searchemp'),
]