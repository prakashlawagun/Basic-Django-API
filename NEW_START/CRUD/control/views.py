from django.shortcuts import render, redirect
from .models import User
from .forms import EmployeeRegister


# Create your views here.

def index(request):
    emp = User.objects.all()
    context = {
        'employee': emp
    }
    return render(request, 'index.html', context)


def addEmployee(request):
    if request.method == 'POST':
        fm = EmployeeRegister(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ad = fm.cleaned_data['address']
            ph = fm.cleaned_data['phone']
            reg = User(name=nm, email=em, address=ad, phone=ph)
            reg.save()
            return redirect('control:index')
    else:
        fm = EmployeeRegister()
    context = {
        'form': fm,
    }
    return render(request, 'add.html', context)


def deleteEmployee(request, id):
    pi = User.objects.filter(pk=id)
    pi.delete()
    return redirect('control:index')


def viewEmployee(request, id):
    employee = User.objects.get(pk=id)
    context = {
        'employee': employee
    }
    return render(request, 'show.html', context)


def editEmployee(request, id):
    if request.method == 'POST':
        employee = User.objects.get(pk=id)
        fm = EmployeeRegister(request.POST, instance=employee)
        if fm.is_valid():
            fm.save()
    else:
        employee = User.objects.get(pk=id)
        fm = EmployeeRegister(instance=employee)

    context = {
        'form': fm
    }
    return render(request, 'edit.html', context)


def searchEmployee(request):
    query = request.GET['query']
    allData = User.objects.filter(name__icontains=query) | User.objects.filter(phone__icontains=query)

    context = {
        'allData': allData
    }
    return render(request, 'search.html', context)
