from django.urls import path
from . import views

urlpatterns = [
    path('terminals/', views.index, name='terminals'),
    path('terminals/<int:terminal_id>/', views.detail, name='terminal_detail'),
    path('api/terminals/', views.TerminalsAPIView.as_view(), name='terminals-api'),
    path('api/terminals/<int:pk>/', views.TerminalDetailsAPIView.as_view(), name='terminal-details-api'),
]
