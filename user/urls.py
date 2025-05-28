#campings app urls.py
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'user'

urlpatterns = [
    path('logout_view' , views.logout_view , name='logout_view'),
    path('login_view' , views.login_view ,  name='login_view'),
    path('register_view' , views.register_view , name='register_view')
]
