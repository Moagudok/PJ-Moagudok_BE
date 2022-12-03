from django.conf import settings
import os

# 디버깅 관련
DEBUG_PRINT = True

# IP
AWS_AUTH_IP = os.environ.get('AWS_HOST') + ':' + os.environ.get('AWS_AUTH_SVC_PORT')
AWS_SELLER_IP = os.environ.get('AWS_HOST') + ':' + os.environ.get('AWS_SELLER_SVC_PORT')
AWS_PAYMENT_IP = os.environ.get('AWS_HOST') + ':' + os.environ.get('AWS_PAYMENT_SVC_PORT')
