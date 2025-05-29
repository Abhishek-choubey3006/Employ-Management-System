from datetime import datetime, timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):

    Feature_image = models.ImageField(
        upload_to='media/Employee', blank=False, null=False)
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    STATUS_CHOICES = [('Active', 'Active'), ('Inactive', 'Inactive')]
    Department = [
        ('UI/UX', 'UI/UX'), ('Development', 'Development'),
        ('Management', 'Management'), ('HR', 'HR'),
        ('Testing', 'Testing'), ('Marketing', 'Marketing'),
    ]
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='staff_profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdaydate = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department = models.CharField(
        choices=Department, default='Development', max_length=100)
    position = models.CharField(max_length=100)
    hire_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='Active')
    Educations = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    Company = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} "

# Leave Form 


class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    STATUS_CHOICES = [('Pending', 'Pending'), ('Approved','Approved'), ('Rejected', 'Rejected')]
    CHOICES = [('Admin', 'Admin'), ('Employee', 'Employee')]
    
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    target = models.CharField( max_length=50, choices=CHOICES, default='Employee')
    
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee.first_name} - {self.status}"

    @property
    def leave_days(self):
        return (self.end_date - self.start_date).days + 1


class LeaveRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    total_leaves = models.IntegerField()
    taken = models.IntegerField()
    absent = models.IntegerField()
    request = models.IntegerField()
    worked_days = models.IntegerField()
    loss_of_pay = models.IntegerField()

