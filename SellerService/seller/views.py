from rest_framework import status, exceptions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from sharedb.models import Product, ProductImages, Category, PaymentTerm, User

from .serializers import ProductSerializer

# pagenation 페이지 별 상품의 개수
STANDARD_NUM_OF_PRODUCTS = 10


class ProductView(APIView):
    # url = /seller/product/1?page=1&filter="views"&?"group_name"="돼지좋아"
    def get(self, request: Request, seller_id) -> ProductSerializer:

        page_num = int(request.query_params["page"])
        filter = request.query_params["filter"]
        firter_list = ["recent", "views", "subscribers"]

        # 만약 판매중인 구독 상품에서 그룹을 누른다면 그룹별 수정 페이지로 전환
        group_name = request.query_params.get("group_name", None)
        
        if group_name:
            sellers_product_all_query = Product.objects.filter(seller=seller_id, product_group_name = group_name)
            is_grouped = True
        else :
            sellers_product_all_query = Product.objects.filter(seller=seller_id)
            is_grouped = False
        sellers_product_count = sellers_product_all_query.count()


        # 최대 페이지 수, 필터링 단어 제한
        total_page = sellers_product_count // STANDARD_NUM_OF_PRODUCTS + 1
        if total_page < page_num or filter not in firter_list:
            return Response({"detail": "해당 페이지에 데이터가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        # filtering
        if filter == "recent":
            filtering_product_query = sellers_product_all_query.order_by(
                "-update_date")
        elif filter == "views":
            filtering_product_query = sellers_product_all_query.order_by(
                "-views")
        elif filter == "subscribers":
            filtering_product_query = sellers_product_all_query.order_by(
                "-num_of_subscribers")

        # Pagenation
        if sellers_product_count <= STANDARD_NUM_OF_PRODUCTS:
            pagenated_sellers_product_query = filtering_product_query
        else:
            pagenated_sellers_product_query = filtering_product_query[(
                page_num-1) * STANDARD_NUM_OF_PRODUCTS: (page_num-1) * STANDARD_NUM_OF_PRODUCTS + STANDARD_NUM_OF_PRODUCTS]
        sellers_product_serializer = ProductSerializer(
            pagenated_sellers_product_query, many=True).data
        return Response({
            "sellers_products": sellers_product_serializer,
            "total_page": total_page,
            "is_grouped" : is_grouped
        }, status=status.HTTP_200_OK)

    # url = /seller/product
    def post(self, request: Request) -> Response:
        try:
            product_obj_list = []
            detail_image_list = []
            for data in request.data:
                product_obj = Product(
                    seller = User.objects.get(id = 1),  # seller
                    category = Category.objects.get(id = int(data["category"])),  # category
                    product_group_name = data["product_group_name"],  # product_group_name
                    product_name = data["product_name"],  # product_name
                    payment_term = PaymentTerm.objects.get(id = int(data["payment_term"])),  # payment_term
                    register_date = "",  # register_date
                    update_date = "",  # update_date
                    price = data["price"],  # price
                    image = data["image"],  # image
                    description = data["description"],  # description
                )
                
                product_obj_list.append(product_obj)
                
                
                for detail_image in data["detail_images"]:
                    detail_image_obj = ProductImages(image = detail_image, product = product_obj)
                    detail_image_list.append(detail_image_obj)
            Product.objects.bulk_create(product_obj_list)
            ProductImages.objects.bulk_create(detail_image_list)
            

            return Response({"detail": "상품이 등록 되었습니다."}, status=status.HTTP_201_CREATED)
        except exceptions.ValidationError as e:
            error_message = "".join(
                [str(value) for values in e.detail.values() for value in values])
            return Response({"detail": error_message}, status=status.HTTP_400_BAD_REQUEST)


        