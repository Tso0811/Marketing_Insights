#campings app urls.py
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'user'

urlpatterns = [
    path('logout_view' , views.logout_view , name='logout_view')
]
