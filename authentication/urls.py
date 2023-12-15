from .views import RegisterView, login_user
from django.urls import path

urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('',login_user, name='login'),
]