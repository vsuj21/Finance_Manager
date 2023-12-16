from .import views
from django.urls import path


urlpatterns = [

    path('register/', views.register_user, name='register'),
    path('',views.login_user, name='login'),
    path('signout/',views.logout_user, name='signout'),
    path('register/',views.register_user,name='register'),
]