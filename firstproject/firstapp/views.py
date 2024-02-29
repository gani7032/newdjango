from django.shortcuts import render

# Create your views here.
from firstapp.models import employee
def empdata(request):
    emp_list=employee.objects.all()
    return render(request,"emp.html",{"emp_list":emp_list})
