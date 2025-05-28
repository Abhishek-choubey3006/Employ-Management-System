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
