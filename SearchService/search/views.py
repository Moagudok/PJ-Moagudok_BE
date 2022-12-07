from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ErrorDetail
from rest_framework import status
from django.db import transaction
from datetime import datetime
from .db import MongoConnectorbySingleton
from utils import get_userinfo
from constants import RECENT_TEXT_COUNT, TOPHITS_TEXT_COUNT, DEBUG_PRINT

from datetime import datetime, timedelta
import json
from bson import json_util

# url : /search/latest
class SearchLatestTextListView(APIView):
    @transaction.atomic
    def post(self, request):
        search_text = self.request.data['search']

        db_obj = MongoConnectorbySingleton()
        db_col = db_obj.collection

        user_id = get_userinfo(request)
        if user_id == None:
            return Response({'detail':'User not logged in'}, status=status.HTTP_200_OK)
        is_searched = db_col.find_one({'user_id':user_id, 'searchText':search_text})
        if is_searched == None:
            db_col.insert_one(
                {'user_id' : user_id,'searchText': search_text,'dt': datetime.now()},
            )
        else:
            db_col.update_one(
                {'_id':is_searched['_id']}, 
                {'$set':{'dt':datetime.now()}}
            )
        return Response({'detail':'success'}, status=status.HTTP_201_CREATED)

    def get(self, request):
        db_obj = MongoConnectorbySingleton()
        db_col = db_obj.collection
        user_id = get_userinfo(request)
        if user_id == None:
            return Response(ErrorDetail(string='Auth Service is not working', code=500),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        recent_searchs = list(db_col.find( {'user_id': user_id }, {'_id':False} ).limit(RECENT_TEXT_COUNT).sort('dt', -1)) # 
        results =  json.dumps(recent_searchs, default=json_util.default)
        return Response(results, status=status.HTTP_200_OK)

# url : /search/tophits
class SearchTopHitTextListView(APIView):
    def get(self, request):
        db_obj = MongoConnectorbySingleton()
        db_col = db_obj.collection
 
        pipeline = [
            { # 조건
                '$match': {'dt': {'$gte':datetime.now() - timedelta(weeks=1)}}
            },  
            { # grouping
                '$group': {
                    '_id': '$searchText', # searchText 로
                    'count': {'$sum': 1} # counting
                }
            },
            { # 정렬
                '$sort': {'count' : -1} # 내림차순
            }
        ]

        # aggreagte의 제약 가능한 메모리 조작은 100MB로, 초과시 allowDiskUse=True 지정 필요
        tophits_search_text = list(db_col.aggregate(pipeline))[:TOPHITS_TEXT_COUNT] # 10개
        if DEBUG_PRINT: print('tophits_search_text', tophits_search_text)
        results =  json.dumps(tophits_search_text, default=json_util.default)
        return Response(results, status=status.HTTP_200_OK)