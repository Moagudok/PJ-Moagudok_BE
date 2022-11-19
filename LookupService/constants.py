from django.conf import settings
import os

# Cookie Constant
COOKIE_KEY_NAME = 'visitedproduct'
EXPIRED_TIME = 7 

# 기본적으로 출력되어야 하는 상품 갯수 
STANDARD_NUM_OF_PRODUCTS  = 10

# Pagination 크기
PER_PAGE_SIZE = 10

# 검색 관련
RECENT_TEXT_COUNT = 10 # 최근 검색어 갯수
TOPHITS_TEXT_COUNT = 10 # 가장 많이 검색한 갯수

# 디버깅 관련
DEBUG_PRINT = True

# 상품 Detail 정보
OTHER_PRODUCTS_NUM_IN_SELLER = 5

# IP
AWS_IP = os.environ.get('AWS_HOST') + ':' + os.environ.get('AWS_PAYMENT_SVC_PORT')
