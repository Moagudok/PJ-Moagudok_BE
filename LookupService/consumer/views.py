from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from sharedb.models import Category, Product
from .serializers import ProductCategoryListSerializer, ProductListSerializer

# url : /consumer/product/category
class ProductCategoryListView(APIView):
    def get(self, request):
        category_data = Category.objects.all()
        CategorySerializer_data = ProductCategoryListSerializer(category_data, many=True).data
        return Response(CategorySerializer_data, status.HTTP_200_OK)

class ProductListPaginationClass(PageNumberPagination): # 
    page_size = 2 # settings.py의 Default 값 변경

# url : /consumer/product/list?category=1&search&page=1
class ProductListPaginationViewSet(viewsets.ModelViewSet):
    serializer_class = ProductListSerializer
    pagination_class = ProductListPaginationClass
    queryset = Product.objects.all()
    def get_queryset(self):
        condition = Q()
        category_id = self.request.query_params['category']
        search_text = self.request.query_params['search']
        if category_id:
            condition.add(Q(category_id = category_id), condition.AND)
        if search_text:
            mini_q = Q()
            mini_q.add(Q(product_name__icontains = search_text), condition.OR) # product_name - 대소문자 구분 X 검색
            mini_q.add(Q(product_group_name__icontains = search_text), condition.OR) # product_group_name - 대소문자 구분 X 검색
            condition.add(mini_q, condition.AND)
        query_set = self.queryset.filter(condition)
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
