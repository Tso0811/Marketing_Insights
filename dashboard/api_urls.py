#dashboard app api_urls.py
from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter
app_name = 'api_dashboard'

router = DefaultRouter()
router.register(r'campaigns',views.campaign_viewsets)



urlpatterns = [
    path('', include(router.urls)),
]
