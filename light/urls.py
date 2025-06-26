from django.contrib import admin
from django.urls import path, include
from .views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    path('', include('apps.terminals.urls')),
    path('admin/', admin.site.urls),
]
