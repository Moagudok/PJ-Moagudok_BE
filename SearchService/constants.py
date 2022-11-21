from django.conf import settings
import os

# 검색 관련
RECENT_TEXT_COUNT = 10 # 최근 검색어 갯수
TOPHITS_TEXT_COUNT = 10 # 가장 많이 검색한 갯수

# 디버깅 관련
DEBUG_PRINT = True

# IP
AWS_AUTH_IP = os.environ.get('AWS_HOST') + ':' + os.environ.get('AWS_AUTH_SVC_PORT')
