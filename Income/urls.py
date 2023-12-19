from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='incomes'),
    path('add_income', views.add_income, name='add_income'),
    path('edit_income/<int:id>', views.edit_income, name='edit_income'),
    path('delete_income/<int:id>', views.delete_income, name='delete_income'),
    path('income_vis/', views.income_vis_all, name='income_vis'),
    path('income_vis/<str:filter_type>/', views.income_vis, name='get_income_data'),
    
]