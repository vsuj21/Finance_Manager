from django.shortcuts import redirect, render
from .models import Expense, Category
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
from django.http import HttpResponse, JsonResponse
import json
from django.utils.dateparse import parse_date
# Create your views here.

@login_required(login_url='login')
def index(request):
    
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

        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'expenses/add_expense.html', context)
        Expense.objects.create(
            amount=amount,
            description=description,
            owner=request.user,
            title=category,
            date=date,
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




def get_expense_data(request, filter_type):
    today = timezone.now().date()

    if filter_type == 'all':
        expenses = Expense.objects.filter(owner=request.user).order_by('-date')
        
    elif filter_type == 'last_month':
        last_month = today - timedelta(days=today.day)
        expenses = Expense.objects.filter(owner=request.user, date__gte=last_month).order_by('-date')
    elif filter_type == 'past_six_months':
        six_months_ago = today - timedelta(days=180)
        expenses = Expense.objects.filter(owner=request.user, date__gte=six_months_ago).order_by('-date')
    elif filter_type == 'last_year':
        last_year = today - timedelta(days=365)
        expenses = Expense.objects.filter(owner=request.user, date__gte=last_year).order_by('-date')
    else:
        expenses = []

    # Extract amounts and titles into separate lists
    expense_amounts = [float(expense.amount) for expense in expenses]
    expense_titles = [expense.title for expense in expenses]

    data = {
        'expense_data': expense_amounts,
        'expense_labels': expense_titles,
    }

    
    return data
@login_required(login_url='login')
def expense_vis(request, filter_type):
    context = get_expense_data(request, filter_type)
    print(context)
    return JsonResponse(json.dumps(context),safe=False)
    
@login_required(login_url='login')
def expense_vis_all(request):
    context = get_expense_data(request, 'last_month')
    return render(request, 'dashboard/expense.html', {'context': json.dumps(context)})