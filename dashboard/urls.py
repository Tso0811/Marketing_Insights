#campings app urls.py
from django.contrib import admin
from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter
app_name = 'dashboard'

router = DefaultRouter()
router.register(r'campaigns',views.campaign_viewsets)



urlpatterns = [
    path('' , views.show_campaigns , name='show_campaigns'),
    path('campaign_edit/<int:id>/' , views.edit_campaigns , name='campaign_edit'),
    path('campaign_create/' , views.campaign_create , name='campaign_create'),
    path('campaign_delete/<int:id>/' , views.campaign_delete , name='campaign_delete'),
    path('campaign_click/<int:id>/' , views.campaign_click , name='campaign_click'),
    path('postercampaigns/<str:poster>' , views.postercampaigns , name='postercampaigns'),
    path('', include(router.urls)),
]
