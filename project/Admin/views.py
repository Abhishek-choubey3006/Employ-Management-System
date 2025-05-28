from django.shortcuts import render

# Create your views here.
def AdminPage(request):
    return render(request,"../template/Admin/Admin.html")