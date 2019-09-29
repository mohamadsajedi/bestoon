from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

@csrf_exempt
def submit_expense(request):
    """ Submit an Expense """

    this_token = request.POST['Token']
    this_user = User.objects.filter(token__token = this_token).get()
    now = datetime.datetime.now()
    Expense.objects.create(user = this_user, amount=request.POST['amount'], 
                    desc=request.POST['desc'], date=now)
    return JsonResponse({
        'status': 'ok' ,
    })
