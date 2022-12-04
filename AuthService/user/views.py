from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions, serializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from sharedb.models import User as UserModel
from .serializers import UserSerializer, LoginUserSerializer

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import requests
import json

from constrants import AWS_IP

# user/login
class LoginUserAPIView(APIView):
    
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data # Fetch the data form serializer

        user = authenticate(email=data['email'], password=data['password']) # check for email and password
        if not user or user.is_seller != data['is_seller']: # check for phone
            raise serializers.ValidationError({'detail':'지정된 자격 증명에 해당하는 활성화된 사용자를 찾을 수 없습니다'})

        # Generate Token
        refresh = RefreshToken.for_user(user)

        # add payload here!!
        refresh['email'] = data['email']

        return Response(
            {
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }
            , status=status.HTTP_200_OK
            )

# user/join
class JoinUserAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save();
            return Response({"user" : user_serializer.data, "msg" : "회원가입 완료"}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# user
class UserAPIView(APIView):
    # JWT 인증방식 클래스 지정하기
    permission_classes = [permissions.AllowAny]
    
    # 로그인 한 유저 정보 출력
    def get(self, request):
        user = UserModel.objects.get(id=request.user.id)
        response = requests.get('http://'+AWS_IP+'/payment/consumer/mypage?consumerId='+str(request.user.id)+'&type=sub')
        product_list = json.loads(response.text)
        user_serializer = UserSerializer(user).data
        user_serializer['sub_product'] = list(map(int, product_list[0].keys()));
        return Response(user_serializer, status=status.HTTP_200_OK)

class UserInfoAPIView(APIView):
    def get(self, request, id):
        user = UserModel.objects.get(id=id);
        user_serializer = UserSerializer(user).data
        return Response(user_serializer['email'], status=status.HTTP_200_OK)
    