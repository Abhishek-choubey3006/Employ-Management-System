from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Leave
from .forms import *
from datetime import datetime
# Create your views here.
def EmployeePage(request):

    form = LeaveForm()

    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = request.user
            leave.no_of_days = (leave.end_date - leave.start_date).days + 1
            leave.save()
            messages.success(request, 'Leave request submitted successfully!')
            
            
    leaves = Leave.objects.filter(employee=request.user).order_by('-created_at')

    
    return render(request,"../template/Employee/Employee.html", {
        'form': form,
        'leaves': leaves,
    })


