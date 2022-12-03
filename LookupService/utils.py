import json
import requests
from constants import AWS_AUTH_IP, AWS_PAYMENT_IP
from django.conf import settings

def get_userinfo(request):
    # get token
    headers = { "Authorization" : request.headers['Authorization']}

    mode = getattr(settings, 'MODE', 'PRODUCTION')  
    print('====mode:', mode)
    if mode == 'PRODUCTION':
        url = 'http://' + AWS_AUTH_IP + '/user'
    else:
        url = 'http://127.0.0.1:8000/user'

    # TO Auth Service
    try:
        response = requests.get(url, headers=headers)            
        user_id = json.loads(response.text)['id']
    except:
        user_id = None
    return user_id

def get_payment_info(seller_id, month):
    mode = getattr(settings, 'MODE', 'PRODUCTION')  
    print('====mode:', mode)
    if mode == 'PRODUCTION':
        url = 'http://' + AWS_PAYMENT_IP + '/payment/dashboard?sellerId=' + seller_id + '&month=' + month
    else:
        url = 'http://127.0.0.1:8080//payment/dashboard?sellerId=' + seller_id + '&month=' + month
    response = requests.get(url)
    
    return response

def get_monthly_payment_by_year(seller_id, year):
    mode = getattr(settings, 'MODE', 'PRODUCTION')  
    print('====mode:', mode)
    if mode == 'PRODUCTION':
        url = 'http://' + AWS_PAYMENT_IP + '/payment/dashboard?sellerId=' + seller_id + '&year=' + year
    else:
        url = 'http://127.0.0.1:8080/payment/dashboard/monthly?sellerId=' + seller_id + '&year=' + year
    
    response = requests.get(url)
    
    return response

def get_daily_payment_by_month(seller_id, year, month):
    mode = getattr(settings, 'MODE', 'PRODUCTION')  
    print('====mode:', mode)
    if mode == 'PRODUCTION':
        url = 'http://' + AWS_PAYMENT_IP + '/payment/dashboard?sellerId=' + str(seller_id) + '&year=' + str(year)
    else:
        url = 'http://127.0.0.1:8080/payment/dashboard/daily?sellerId=' + str(seller_id) + '&year=' + str(year) + '&month=' + str(month)
    response = requests.get(url)
    
    
    return response

def get_product_newbie():
    mode = getattr(settings, 'MODE', 'PRODUCTION')  
    print('====mode:', mode)
    if mode == 'PRODUCTION':
        url = 'http://' + AWS_PAYMENT_IP + '/payment/dashboard/newbie'
    else:
        url = 'http://127.0.0.1:8080/payment/dashboard/newbie'
    response = requests.get(url)
    
    return response