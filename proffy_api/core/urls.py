from core import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('classes/', views.ClassCreateListAPIView.as_view(), name='class-create-list'),
    path('connections/', views.ConnectionListCreateAPIView.as_view(), name='connection-create-list'),
]
