from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Income.views import  get_income_data
from expenses.views import get_expense_data
from django.utils import timezone
from datetime import timedelta
import json
from django.http import JsonResponse

@login_required(login_url='login')
def index(request, filter_type):
    expense_data = get_expense_data(request, filter_type)
    income_data = get_income_data(request, filter_type)

    context = {
        'expense_data': json.dumps(expense_data),
        'income_data': json.dumps(income_data),
    }

    print(context)
    return JsonResponse(json.dumps(context),safe=False)

@login_required(login_url='login')
def dashboard(request):
    expense_data = get_expense_data(request, 'last_month')
    income_data = get_income_data(request, 'last_month')

    context = { 
        'expense_data': json.dumps(expense_data),
        'income_data': json.dumps(income_data),
    }
    print(context)
    return render(request, 'dashboard/index.html', {'context': json.dumps(context)})
