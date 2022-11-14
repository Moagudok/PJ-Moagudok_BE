from django.db import transaction

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
            sellers_product_all_query = Product.objects.filter(
                seller=seller_id, product_group_name=group_name, is_active=True)
            is_grouped = True
        else:
            sellers_product_all_query = Product.objects.filter(
                seller=seller_id, is_active=True)
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
            "is_grouped": is_grouped
        }, status=status.HTTP_200_OK)

    # url = /seller/product
    @transaction.atomic
    def post(self, request: Request) -> Response:
        try:
            product_obj_list = []
            detail_image_list = []
            for data in request.data:
                product_obj = Product(
                    seller=User.objects.get(id=1),  # seller
                    category=Category.objects.get(
                        id=int(data["category"])),  # category
                    # product_group_name
                    product_group_name=data["product_group_name"],
                    product_name=data["product_name"],  # product_name
                    payment_term=PaymentTerm.objects.get(
                        id=int(data["payment_term"])),  # payment_term
                    register_date="",  # register_date
                    update_date="",  # update_date
                    price=data["price"],  # price
                    image=data["image"],  # image
                    description=data["description"],  # description
                )

                product_obj_list.append(product_obj)

                for detail_image in data["detail_images"]:
                    detail_image_obj = ProductImages(
                        image=detail_image, product=product_obj)
                    detail_image_list.append(detail_image_obj)
            Product.objects.bulk_create(product_obj_list)
            ProductImages.objects.bulk_create(detail_image_list)

            return Response({"detail": "상품이 등록 되었습니다."}, status=status.HTTP_201_CREATED)
        except exceptions.ValidationError as e:
            error_message = "".join(
                [str(value) for values in e.detail.values() for value in values])
            return Response({"detail": error_message}, status=status.HTTP_400_BAD_REQUEST)

    # url = product/<int:seller_id>/<str:group_name>
    @transaction.atomic
    def put(self, request: Request, seller_id: int, group_name: str) -> Response:

        create_product_obj_list = []
        update_product_obj_list = []
        create_detail_image_list = []
        update_detail_image_list = []
        delete_detail_image_list = []

        # 업데이트 (수정 or 삭제)를 담당하는 로직
        for data in request.data["update_product_list"]:
            update_product_obj = Product(
                id=data["id"],
                seller=User.objects.get(id=1),  # seller
                category=Category.objects.get(
                    id=int(data["category"])),  # category
                # product_group_name
                product_group_name=data["product_group_name"],
                product_name=data["product_name"],  # product_name
                payment_term=PaymentTerm.objects.get(
                    id=int(data["payment_term"])),  # payment_term
                register_date="",  # register_date
                update_date="",  # update_date
                price=data["price"],  # price
                image=data["image"],  # image
                description=data["description"],  # description
                is_active=data["is_active"]
            )

            update_product_obj_list.append(update_product_obj)
            
            # 해당 상품에 업데이트 전 상세이미지에 관련된 정보를 불러옴
            before_image_querys = ProductImages.objects.filter(
                product=data["id"])

            # Product의 Detail_image의 개수가 같아서 bulk_update를 진행하면 될 경우 ex) 2개에서 2개로 수정
            if before_image_querys.count() == len(data["detail_images"]):

                for detail_image in data["detail_images"]:
                    for before_image in before_image_querys:
                        update_detail_image_obj = ProductImages(
                            id=before_image.id, image=detail_image, product=update_product_obj)
                        update_detail_image_list.append(
                            update_detail_image_obj)

            # Product의 Detail_image의 개수가 0에서 증가할 경우 ex) 0개에서 3개
            elif before_image_querys.count() == 0:
                for detail_image in data["detail_images"]:
                    create_detail_image_obj = ProductImages(
                        image=detail_image, product=update_product_obj)
                    create_detail_image_list.append(create_detail_image_obj)

            # Product의 Detail_image를 모두 삭제하는 경우
            elif len(data["detail_images"]) == 0:
                delete_detail_image_list = [ProductImages(
                    id=before_image.id) for before_image in before_image_querys]

            # Product의 Detail_image의 개수가 줄어든 경우 ex) 2개였는데 1개로
            elif before_image_querys.count() > len(data["detail_images"]):
                for detail_image in data["detail_images"]:
                    for index, before_image in enumerate(before_image_querys):
                        if index+1 <= before_image_querys.count():
                            update_detail_image_obj = ProductImages(
                                id=before_image.id, image=detail_image, product=update_product_obj)
                            update_detail_image_list.append(
                                update_detail_image_obj)
                        else:
                            delete_detail_image_obj = [
                                ProductImages(id=before_image.id)]
                            delete_detail_image_list.append(
                                delete_detail_image_obj)

            # Product의 Detail_image의 개수가 증가한 경우 ex) 1개였는데 3개로
            elif before_image_querys.count() < len(data["detail_images"]):
                for index, detail_image in enumerate(data["detail_images"]):
                    for before_image in before_image_querys:
                        if index+1 <= before_image_querys.count() or before_image_querys.count() == 0:
                            update_detail_image_obj = ProductImages(
                                id=before_image.id, image=detail_image, product=update_product_obj)
                            update_detail_image_list.append(
                                update_detail_image_obj)
                        else:
                            create_detail_image_obj = ProductImages(
                                image=detail_image, product=update_product_obj)
                            create_detail_image_list.append(
                                create_detail_image_obj)
                            
        # 업데이트에서 새로운 상품을 추가하는 경우
        for data in request.data["create_product_list"]:
            product_obj = Product(
                seller=User.objects.get(id=1),  # seller
                category=Category.objects.get(
                    id=int(data["category"])),  # category
                # product_group_name
                product_group_name=data["product_group_name"],
                product_name=data["product_name"],  # product_name
                payment_term=PaymentTerm.objects.get(
                    id=int(data["payment_term"])),  # payment_term
                register_date="",  # register_date
                update_date="",  # update_date
                price=data["price"],  # price
                image=data["image"],  # image
                description=data["description"],  # description
            )

            create_product_obj_list.append(product_obj)

            for detail_image in data["detail_images"]:
                detail_image_obj = ProductImages(
                    image=detail_image, product=product_obj)
                create_detail_image_list.append(detail_image_obj)
            
        # 상품 생성
        Product.objects.bulk_create(create_product_obj_list)
        #상품 업데이트(수정, 삭제)
        Product.objects.bulk_update(update_product_obj_list, [
                                    "category", "product_group_name", "product_name", "payment_term", "price", "image", "description", "is_active"])
        # 상품 상세 이미지 삭제
        [ProductImages(id=delete_image.id).delete() for delete_image in delete_detail_image_list]
        # 상품 상세 이미지 업데이트
        ProductImages.objects.bulk_update(update_detail_image_list, ["image"])
        # 상품 상세 이미지 생성
        ProductImages.objects.bulk_create(create_detail_image_list)
        return Response({"detail": "상품이 업데이트 되었습니다."}, status=status.HTTP_200_OK)
