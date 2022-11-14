from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ErrorDetail

from datetime import datetime
from .db import MongoConnectorbySingleton
import json
from bson import json_util

# url : /search/latest
class SearchLatestTextListView(APIView):
    def post(self, request):
        search_text = self.request.data['search']

        db_obj = MongoConnectorbySingleton()
        print('======', db_obj)
        db_col = db_obj.collection
        
        is_searched = db_col.find_one({'searchText':search_text})
        if is_searched == None:
            db_col.insert_one(
                {'username' : 1,'searchText': search_text,'dt': datetime.now()},
            )
        else:
            db_col.update_one({'_id':is_searched['_id']}, {'$set':{'dt':datetime.now()}})
        return Response({'detail':'success'}, status=status.HTTP_201_CREATED)


    def get(self, request):
        RECENT_TEXT_COUNT = 10
        db_obj = MongoConnectorbySingleton()
        db_col = db_obj.collection
        recent_searchs = list(db_col.find( {'username':1}, {'_id':False} ).limit(RECENT_TEXT_COUNT).sort('dt', -1)) # 


        results =  json.dumps(recent_searchs, default=json_util.default)
        return Response(results, status=status.HTTP_200_OK)

        # db_col.insert_many([
        #     {'username' : 1,'searchText': 'abcd','datetime': datetime.now()},
        #     {'username' : 1,'searchText': 'abcd'+'2','datetime': datetime.now()},
        #     {'username' : 1,'searchText': 'abdc'+'3','datetime': datetime.now()},
        # ])