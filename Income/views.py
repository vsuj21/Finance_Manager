from django.shortcuts import redirect, render
from .models import Income, Income_Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
import json
from datetime import datetime, timedelta
# Create your views here.

@login_required(login_url='login')
def index(request):
    
    incomes = Income.objects.filter(owner=request.user)
    context = {
       
        'incomes': incomes
    }
    return render(request, 'incomes/index.html',context)
def add_income(request):
    Categories = Income_Category.objects.all()
    context ={
        'Categories': Categories,
        'values': request.POST        
        
    }
    
    
    if request.method == 'GET':
        
         return render(request, 'incomes/add_income.html',context)
    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'incomes/add_income.html',context)
        
        
        description = request.POST['description']

        if not description:
            messages.error(request, 'description is required')
            return render(request, 'incomes/add_income.html',context)
        category = request.POST['category']
        date = request.POST['date']

        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'incomes/add_income.html', context)
    
        Income.objects.create(
            amount=amount,
            description=description,
            owner=request.user,
            title=category,
            date=date,
        )
        messages.success(request, 'Income saved successfully')
        return redirect('incomes')

def edit_income(request,id):
    categories = Income_Category.objects.all()
    income = Income.objects.get(pk=id)
    context ={
        'income': income,
        'values': income,
        'categories': categories,
    }

    if request.method == 'GET':
        
        return render(request, 'incomes/edit_income.html',context)
    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'incomes/edit_income.html',context)
        
        
        description = request.POST['description']

        if not description:
            messages.error(request, 'description is required')
            return render(request, 'incomes/edit_income.html',context)
        category = request.POST['category']
        date = request.POST['date']
        income.amount=amount
        income.description=description
        income.owner=request.user
        income.title=category
        income.date = date
        income.save()
        messages.success(request, 'income updated successfully')
        
        return redirect('incomes')
    
def delete_income(request,id):
    income = Income.objects.get(pk=id)
    income.delete()
    messages.info(request, 'Income deleted successfully')
    return redirect('incomes')


from django.utils import timezone


def get_income_data(request, filter_type):
    today = timezone.now().date()

    if filter_type == 'all':
        incomes = Income.objects.filter(owner=request.user).order_by('-date')
        
    elif filter_type == 'last_month':
        last_month = today - timedelta(days=today.day)
        incomes = Income.objects.filter(owner=request.user, date__gte=last_month).order_by('-date')
    elif filter_type == 'past_six_months':
        six_months_ago = today - timedelta(days=180)
        incomes = Income.objects.filter(owner=request.user, date__gte=six_months_ago).order_by('-date')
    elif filter_type == 'last_year':
        last_year = today - timedelta(days=365)
        incomes = Income.objects.filter(owner=request.user, date__gte=last_year).order_by('-date')
    else:
        incomes = []

    # Extract amounts and titles into separate lists
    income_amounts = [float(income.amount) for income in incomes]
    income_titles = [income.title for income in incomes]

    data = {
        'income_data': income_amounts,
        'income_labels': income_titles,
    }

    
    return data
@login_required(login_url='login')
def income_vis(request, filter_type):
    context = get_income_data(request, filter_type)
    print(context)
    return JsonResponse(json.dumps(context),safe=False)
    
@login_required(login_url='login')
def income_vis_all(request):
    context = get_income_data(request, 'last_month')
    return render(request, 'dashboard/income.html', {'context': json.dumps(context)})