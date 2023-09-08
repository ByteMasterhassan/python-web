from multiprocessing import context
from datetime import datetime
from django.shortcuts import render,HttpResponse
from .models import employee,role,department
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')


def view_emp(request):
    emps=employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'view_emp.html',context)


def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        Phone_number=int (request.POST['Phone_number'])
        
        rol=request.POST['rol']
        dept=request.POST['dept']

        new_emp= employee(first_name=first_name,last_name=last_name,rol__name=rol,Phone_number=Phone_number,
        salary=salary,bonus=bonus,dept__name=dept)

        new_emp.save()

        return HttpResponse('Employee is added successfully!!!')
    elif request.method=='GET':
        return render (request, 'add_emp.html')
    else:
        return HttpResponse('Exception Error Againset your input!!!')


def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        rol=request.POST['rol']
        emps=employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name)| Q(last_name__icontains= name))
        if dept:
            emps=emps.filter(dept__name=dept)
        if rol:
            emps=emps.filter(rol__name=rol)
            
        context= {
            'emps':emps
        }
        print(context)
        return render(request,'view_emp.html',context)
    elif request.method=='GET':
         return render (request, 'filter_emp.html')

    else:
        return HttpResponse('Something goes wrong!!!')


def remove_emp(request,emp_id=0):
    if emp_id: 
        try:
            employee_to_be_removed=employee.objects.get(id=emp_id)
            employee_to_be_removed.delete()
            return HttpResponse('Employee is removed successfully!!!')
        except:
            return HttpResponse('Enter a valid statement!!!')

    emps=employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render (request, 'remove_emp.html',context)