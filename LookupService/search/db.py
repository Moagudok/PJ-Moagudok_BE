from pymongo import MongoClient
from django.conf import settings
import os

class MongoConnectorbySingleton(object):
    # __new__, 이 __init__ 보다 먼저 실행됨
    def __new__(cls, *args, **kwargs): 
        if not hasattr(cls, "_instance"):           # _instance 속성 : Singleton 객체
            print("__new__ is called")
            cls._instance = super().__new__(cls)    # 객체 생성 및 _instacne key로 바인딩
        return cls._instance                        # _instance return

    def __init__(self, **kwargs):
        cls = type(self)
        if not hasattr(cls, "_init"):               # _init 속성 : Singleton 객체 존재 여부 
            print("__init__ is called")
            self.mode = settings.MODE
            print('=========', self.mode)
            if self.mode == 'PRODUCTION':
                self.db_path = os.environ.get('PRODUCTION_MONGO_URL')
                self.client = MongoClient(self.db_path)
            else: # LOCAL or LOCAL_TEST
                self.db_path = "mongodb://" + os.environ.get('MONGO_DB_HOST') +':' + os.environ.get('MONGO_DB_PORT') +'/'
                self.client = MongoClient(self.db_path,
                                        username = os.environ.get('MONGO_USER'),
                                        password = os.environ.get('MONGO_PASSWORD'),
                                        )

            self.db = self.client[os.environ.get('MONGO_DB_NAME')] 
            self.collection = self.db.searchtext
            cls._init = True