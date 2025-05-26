#campings app urls.py
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'dashboard'

urlpatterns = [
    path('' , views.show_campaigns , name='show_campaigns'),
    path('campaign_edit/<int:id>' , views.edit_campaigns , name='campaign_edit'),
    path('campaign_create/' , views.campaign_create , name='campaign_create'),
    path('campaign_delete/<int:id>' , views.campaign_delete , name='campaign_delete'),
    path('campaign_click/<int:id>' , views.campaign_click , name='campaign_click'),
]
