from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from sharedb.models import User as UserModel
from .serializers import UserSerializer


# user/cjoin/
class ConsumerJoinView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"user" : user_serializer.data, "msg" : "회원가입 완료"}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# user/sjoin/
class SellerJoinView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        request.data['is_seller'] = True
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"user" : user_serializer.data, "msg" : "회원가입 완료"}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# user/
class UserAPIView(APIView):
    # JWT 인증방식 클래스 지정하기
    authentication_classes = [JWTAuthentication]
    
    # 로그인 한 유저 정보 출력
    def get(self, request):
        user = UserModel.objects.get(id=request.user.id)        
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
    