import json
import requests

def get_userinfo(request):
    headers = { "Authorization" : request.headers['Authorization']}
    # TO Auth Service
    user_id = None
    try:
        response = requests.get('http://127.0.0.1:8000/user', headers=headers)            
        user_id = json.loads(response.text)['id']
    except:
        user_id = None
    return user_id