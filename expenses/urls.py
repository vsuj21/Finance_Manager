from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='expenses'),
    path('add_expense', views.add_expense, name='add_expense'),
    path('edit_expense/<int:id>', views.edit_expense, name='edit_expense'),
    path('delete_expense/<int:id>', views.delete_expenses, name='delete_expense'),
    path('expense_vis/', views.expense_vis_all, name='expense_vis'),
    path('expense_vis/<str:filter_type>/', views.expense_vis, name='get_expense_data'),
]