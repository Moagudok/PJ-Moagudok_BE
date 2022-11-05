from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from sharedb.models import Category

# url : /consumer/product/category
class ProductCategoryListView(APIView):
    def get(self, request):
        return Response({}, status.HTTP_200_OK)
        # return Response(room_user_list_serializer_data, status.HTTP_200_OK)