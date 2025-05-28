from django.urls import path 
from Employee.views import *

urlpatterns = [
    path('Emp',EmployeePage,name='EmployeePage')

]