from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination # 페이지 기반 파지네이션 import

from sharedb.models import Category, Product
from .serializers import ProductCategoryListSerializer, ProductListSerializer

# url : /consumer/product/category
class ProductCategoryListView(APIView):
    def get(self, request):
        category_data = Category.objects.all()
        CategorySerializer_data = ProductCategoryListSerializer(category_data, many=True).data
        return Response(CategorySerializer_data, status.HTTP_200_OK)


class CategoryListPaginationClass(PageNumberPagination): # 
    page_size = 2 # settings.py의 Default 값 변경

# url : /consumer/product/list?category=1&page=1
class CategoryListPaginationViewSet(viewsets.ModelViewSet):
    serializer_class = ProductListSerializer
    pagination_class = CategoryListPaginationClass
    queryset = Product.objects.all()
    def get_queryset(self):
        category_id = self.request.query_params['category']
        query_set = self.queryset.filter(category_id=category_id)
        return query_set


''' legacy code 
def list(self, request):
    category_id = request.query_params['category']
    if not category_id.isdigit():
        return Response({'message':'Params is invalid'}, status.HTTP_400_BAD_REQUEST)

    product_data = Product.objects.filter(category_id=category_id)
    if len(product_data) == 0:
        return Response({'message':'There are no products in this category'}, status.HTTP_200_OK)

    ProductSerializer_data = ProductListSerializer(product_data, many=True).data
    return Response(ProductSerializer_data, status.HTTP_200_OK)

    # serializer = UserSerializer(queryset, many=True)
    # return Response(serializer.data)
'''
