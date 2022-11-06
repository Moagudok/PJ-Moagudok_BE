from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from sharedb.models import Category
from .serializers import ProductCategoryListSerializer 

# url : /consumer/product/category
class ProductCategoryListView(APIView):
    def get(self, request):
        category_data = Category.objects.all()
        CategorySerializer_data = ProductCategoryListSerializer(category_data, many=True).data
        return Response(CategorySerializer_data, status.HTTP_200_OK)