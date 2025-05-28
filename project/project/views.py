from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from datetime import date, datetime
from Employee.models import *
from Admin.models import *

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                messages.success(request, "Admin login successful")
                return redirect('admin_page')
            elif user.is_staff:
                if Employee.objects.filter(user=user).exists():
                    messages.success(request, "Employee login successful")
                    return redirect('employee_page')
                else:
                    messages.info(request, 'Please complete your employee profile.')
                    return render(request, '../template/Signup.html')
            else:
                messages.error(request, "No role assigned to this user.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, '../template/LogIn.html')

# ----- Signup View -----
def user_signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if User.objects.filter(email=email).exists():
            messages.error(request, 'User already exists, please login.')
            return redirect('user_login')

        new_user = User.objects.create_user(username=username, email=email, password=password)

        # Handle role flags
        if role == "admin":
            new_user.is_superuser = True
            new_user.is_staff = True
        elif role == "employee":
            new_user.is_staff = True

        new_user.save()

        if role == "employee":
            Employee.objects.create(user=new_user, hire_date=date.today(), email=email)

        messages.success(request, "User registered successfully.")
        return redirect('user_login')

    return render(request, "../template/Signup.html")

# ----- Logout View -----
def user_logout(request):
    auth_logout(request)
    return redirect('user_login')
