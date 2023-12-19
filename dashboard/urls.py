from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/<str:filter_type>/', views.index, name='index'),
]

