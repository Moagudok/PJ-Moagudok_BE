from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response
from rest_framework import status
import json
import requests

def get_userinfo(request):
    headers = { "Authorization" : request.headers['Authorization']}
    # TO Auth Service
    user_id = None
    try:
        response = requests.get('http://127.0.0.1:8000/user', headers=headers)            
        user_id = json.loads(response.text)['id']
        if response.status_code == status.HTTP_404_NOT_FOUND:
            return Response(ErrorDetail(string='URL is invalid', code=404),statuHTTP_404_NOT_FOUND=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except:
        return Response(ErrorDetail(string='Auth Service is not working', code=500),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    print('======', user_id)      
    if user_id==None:
        return Response(ErrorDetail(string='Auth Service is not working', code=500),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return user_id