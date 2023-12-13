from django.shortcuts import redirect, render
from .models import Income, Income_Category
from django.contrib import messages
# Create your views here.
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
        Income.objects.create(
            amount=amount,
            description=description,
            owner=request.user,
            title=category,
            date = date,
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
    