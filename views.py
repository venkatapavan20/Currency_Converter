from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

@csrf_exempt
def currency(request):
    if request.method == 'POST':
        amount = json.loads(request.body)['amount']
                   
        if  'usd_to_inr':
            converted_amount = amount * 82.6  
        #if 'inr_to_usd':
            #converted_amount = amount / 82.6
        else:
            converted_amount = None

        response_data = {'converted_amount': converted_amount}
        return JsonResponse(response_data)
@csrf_exempt
def currency1(request):
    if request.method == 'POST':
        amount1 = json.loads(request.body)['amount1']
      
        if 'inr_to_usd':
            converted_amount = amount1 / 82.6
        else:
            converted_amount = None

        response_data = {'converted_amount': converted_amount}
        return JsonResponse(response_data)


