from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from sharedb.models import Category, Product
from .serializers import ProductCategoryListSerializer, ProductListSerializer

# url : /consumer/product/category
class ProductCategoryListView(APIView):
    def get(self, request):
        category_data = Category.objects.all()
        CategorySerializer_data = ProductCategoryListSerializer(category_data, many=True).data
        return Response(CategorySerializer_data, status.HTTP_200_OK)

# url : /consumer/product/list?category=1
class ProductListView(APIView):
    def get(self, request):
        category_id = request.query_params['category']
        if not category_id.isdigit():
            return Response({'message':'Params is invalid'}, status.HTTP_400_BAD_REQUEST)
        
        product_data = Product.objects.filter(category_id=category_id)
        if len(product_data) == 0:
            return Response({'message':'There are no products in this category'}, status.HTTP_200_OK)
        
        ProductSerializer_data = ProductListSerializer(product_data, many=True).data
        return Response(ProductSerializer_data, status.HTTP_200_OK)
