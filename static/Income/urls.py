from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='incomes'),
    path('add_income', views.add_income, name='add_income'),
    path('edit_income/<int:id>', views.edit_income, name='edit_income'),
    path('delete_income/<int:id>', views.delete_income, name='delete_income'),
]