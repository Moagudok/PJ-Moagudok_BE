import json
import requests
from constants import AWS_AUTH_IP
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
