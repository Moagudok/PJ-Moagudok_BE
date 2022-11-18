from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.views import JoinUserAPIView, UserAPIView, LoginUserAPIView

urlpatterns = [
    path('user', UserAPIView.as_view()),
    path('user/login', LoginUserAPIView.as_view()),
    path('user/join', JoinUserAPIView.as_view(), name='userjoin'),
    path('user/token', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('user/token/refresh', TokenRefreshView.as_view(), name="token_refresh"),
]
