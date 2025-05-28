from django.shortcuts import render

# Create your views here.
def EmployeePage(request):
    return render(request,"../template/Employee/Employee.html")