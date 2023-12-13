from django.shortcuts import redirect, render
from .models import Expense, Category
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    Categories = Category.objects.all()
    expenses = Expense.objects.filter(owner=request.user)
    context = {
       
        'expenses': expenses
    }
    return render(request, 'expenses/index.html',context)
def add_expense(request):
    Categories = Category.objects.all()
    context ={
        'Categories': Categories,
        'values': request.POST        
        
    }
    
    
    if request.method == 'GET':
        
         return render(request, 'expenses/add_expense.html',context)
    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expenses/add_expense.html',context)
        
        
        description = request.POST['description']

        if not description:
            messages.error(request, 'description is required')
            return render(request, 'expenses/add_expense.html',context)
        category = request.POST['category']
        date = request.POST['date']
        Expense.objects.create(
            amount=amount,
            description=description,
            owner=request.user,
            title=category,
            date = date,
        )
        messages.success(request, 'Expense saved successfully')
        return redirect('expenses')

def edit_expense(request,id):
    categories = Category.objects.all()
    expense = Expense.objects.get(pk=id)
    context ={
        'expense': expense,
        'values': expense,
        'categories': categories,
    }
    if request.method == 'GET':
        
        return render(request, 'expenses/edit_expenses.html',context)
    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expenses/edit_expense.html',context)
        
        
        description = request.POST['description']

        if not description:
            messages.error(request, 'description is required')
            return render(request, 'expenses/edit_expense.html',context)
        category = request.POST['category']
        date = request.POST['date']
        expense.amount=amount
        expense.description=description
        expense.owner= request.user
        expense.title=category
        expense.date = date
        expense.save()
        messages.success(request, 'Expense updated successfully')
        return redirect('expenses')
def delete_expenses(request,id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.info(request, 'Expense deleted successfully')
    return redirect('expenses')
    