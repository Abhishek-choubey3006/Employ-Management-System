from django.urls import path 
from Employee.views import *

urlpatterns = [
    path('',EmployeePage,name='employee_page'),

]