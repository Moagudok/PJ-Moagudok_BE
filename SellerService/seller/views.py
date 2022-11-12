from rest_framework import status, exceptions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from sharedb.models import Product, ProductImages

from .serializers import ProductSerializer

# pagenation 페이지 별 상품의 개수
STANDARD_NUM_OF_PRODUCTS = 10


class ProductView(APIView):
    # url = /seller/product/1?page=1&filter="views"
    def get(self, request: Request, seller_id) -> ProductSerializer:

        page_num = int(request.query_params["page"])
        filter = request.query_params["filter"]
        firter_list = ["recent", "views", "subscribers"]

        sellers_product_all_query = Product.objects.filter(seller=seller_id)
        sellers_product_count = sellers_product_all_query.count()

        # 최대 페이지 수, 필터링 단어 제한
        total_page = sellers_product_count // STANDARD_NUM_OF_PRODUCTS + 1
        if total_page < page_num or filter not in firter_list:
            return Response({"detail": "해당 페이지에 데이터가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        # filtering
        if filter == "recent":
            filtering_product_query = sellers_product_all_query.order_by(
                "-register_date")
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
            "total_page": total_page
        }, status=status.HTTP_200_OK)

    # url = /seller/product
    def post(self, request: Request) -> Response:
        try:
            product_data_list = []
            detail_image_data = {}

            for index, data in enumerate(request.data):
                if Product.objects.last():
                    product_id = Product.objects.last().id
                else:
                    product_id = 0
                product_data_list.append(
                    Product(
                        product_id + index + 1,  # id
                        request.user.id,  # seller
                        data["category"],  # category
                        data["product_group_name"],  # product_group_name
                        data["product_name"],  # product_name
                        data["payment_term"],  # payment_term
                        "",  # register_date
                        "",  # update_date
                        data["price"],  # price
                        data["image"],  # image
                        data["description"],  # description
                    )
                )
                # detail_image에 대한 처리를 {product_id : detail_image}로 구성
                detail_image_dict = {
                    str(product_id + index + 1): str(data.pop("detail_images"))}
                detail_image_dict = {**detail_image_data, **detail_image_dict}

            Product.objects.bulk_create(product_data_list)

            detail_images_list = []

            for product_id, images in detail_image_dict.items():
                for image in images:
                    detail_images_list.append(
                        ProductImages(
                            image=image, product=Product.objects.get(id=product_id))
                    )
            ProductImages.objects.bulk_create(detail_images_list)

            return Response({"detail": "상품이 등록 되었습니다."}, status=status.HTTP_201_CREATED)
        except exceptions.ValidationError as e:
            error_message = "".join(
                [str(value) for values in e.detail.values() for value in values])
            return Response({"detail": error_message}, status=status.HTTP_400_BAD_REQUEST)
