from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class MailView(APIView):
    def post(self, request):
        try:
            sender = getattr(settings, 'EMAIL_HOST_USER', None)[0]
            send_mail(
                subject = request.data['subject'],
                message = request.data['message'],
                from_email = sender,
                recipient_list = [email for email in request.data['recipient']],
                fail_silently = False,
            )
            return Response({'detail': '메일 전송 성공'}, status=status.HTTP_200_OK)
            
        except Exception as e :
            return Response({'detail': '메일 전송 실패 ' + e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
