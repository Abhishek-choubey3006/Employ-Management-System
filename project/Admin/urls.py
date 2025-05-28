
from django.urls import path
from Admin.views import *

urlpatterns = [
    path('',AdminPage,name='admin_page')

]