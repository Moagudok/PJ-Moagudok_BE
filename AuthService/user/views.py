from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from user.serializers import UserSignUpSerializers
from rest_framework_simplejwt.views import TokenObtainPairView

class UserView(APIView):
    
    # 회원가입
    def post(self, request):
        try:
            serializer = UserSignUpSerializers(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message":"회원 가입이 완료되었습니다"}, status=status.HTTP_201_CREATED)
        except exceptions.ValidationError:
            return Response({"error":"이메일이 중복되었습니다"}, status=status.HTTP_400_BAD_REQUEST)