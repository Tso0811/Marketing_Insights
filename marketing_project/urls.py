#專案urls.py
from django.contrib import admin
from django.urls import path , include
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('campaigns/' , include('campaigns.urls')),
    path('dashboard/' , include('dashboard.urls')),
    path('user/', include('user.urls')),
    path('api/', include('dashboard.api_urls')),
    path('api-auth/', include('rest_framework.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)