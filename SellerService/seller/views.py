from django.db import transaction

from rest_framework import status, exceptions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from sharedb.models import Product, ProductImages, Category, PaymentTerm, User


from utils import (get_userinfo)




def get_product_obj(data, seller_id, group_name):

    return Product(
        id=data.get("id", None),
        seller=User.objects.get(id=seller_id),  # seller
        category=Category.objects.get(
            id=int(data["category"])),  # category
        # product_group_name
        product_group_name=data.get("product_group_name", group_name),
        product_name=data["product_name"],  # product_name
        subtitle=data["subtitle"],  # product_name
        payment_term=PaymentTerm.objects.get(
            id=int(data["payment_term"])),  # payment_term
        register_date="",  # register_date
        update_date="",  # update_date
        price=data["price"],  # price
        image=data["image"],  # image
        description=data["description"],  # description
    )


def get_detail_image_obj(id, image, product):
    return ProductImages(
        id=id, image=image, product=product)


class ProductView(APIView):
    
    # url = /seller/product
    @transaction.atomic
    def post(self, request: Request) -> Response:

        seller_id = get_userinfo(request)

        try:
            product_obj_list = []
            detail_image_list = []
            for data in request.data:
                product_obj = get_product_obj(data, seller_id, None)

                product_obj_list.append(product_obj)

                for detail_image in data["detail_images"]:
                    detail_image_obj = get_detail_image_obj(
                        None, detail_image, product_obj)
                    detail_image_list.append(detail_image_obj)
            Product.objects.bulk_create(product_obj_list)
            ProductImages.objects.bulk_create(detail_image_list)

            return Response({"detail": "상품이 등록 되었습니다."}, status=status.HTTP_201_CREATED)
        except exceptions.ValidationError as e:
            error_message = "".join(
                [str(value) for values in e.detail.values() for value in values])
            return Response({"detail": error_message}, status=status.HTTP_400_BAD_REQUEST)

    # url = product/<str:group_name>
    @transaction.atomic
    def put(self, request: Request, group_name: str) -> Response:

        seller_id = get_userinfo(request)

        create_product_obj_list = []
        update_product_obj_list = []
        delete_product_obj_list = []
        create_detail_image_list = []
        update_detail_image_list = []
        delete_detail_image_list = []

        grouped_product_query = Product.objects.filter(
            product_group_name=group_name)

        # 업데이트할 상품들
        for data in request.data["update_product_list"]:
            update_product_obj = get_product_obj(data, seller_id, group_name)
            update_product_obj_list.append(update_product_obj)

        # 추가로 생성할 상품들
        for data in request.data["create_product_list"]:
            product_obj = get_product_obj(data, seller_id, group_name)
            create_product_obj_list.append(product_obj)

        # 삭제할 상품들
        for data in request.data["delete_product_list"]:
            product_obj = grouped_product_query.get(id=data["id"])
            delete_product_obj_list.append(product_obj)
            delete_detail_images = ProductImages.objects.filter(
                product=product_obj)
            for detail_image in delete_detail_images:
                delete_detail_image_list.append(detail_image)

        # 업데이트할 상세 이미지들
        for data in request.data["update_detail_image_list"]:
            product_obj = Product.objects.get(id=data["product_id"])
            for index, before_detail_image in enumerate(data["before_detail_images"]):
                image_id = ProductImages.objects.get(
                    image=before_detail_image, product__id = data["product_id"]).id
                update_detail_image_obj = get_detail_image_obj(
                    image_id, data["after_detail_images"][index], product_obj)
                update_detail_image_list.append(update_detail_image_obj)

        # 추가로 생성할 상세 이미지들
        for data in request.data["create_detail_image_list"]:
            product_obj = Product.objects.get(id=data["product_id"])
            for detail_image in data["detail_images"]:
                create_detail_image_obj = get_detail_image_obj(
                    None, detail_image, product_obj)
                create_detail_image_list.append(create_detail_image_obj)

        # 삭제할 상세 이미지들
        for data in request.data["delete_detail_image_list"]:
            product_obj = Product.objects.get(id=data["product_id"])
            for detail_image in data["detail_images"]:
                image_id = ProductImages.objects.get(image=detail_image, product__id = data["product_id"]).id
                delete_detail_image_obj = get_detail_image_obj(
                    image_id, detail_image, product_obj)
                delete_detail_image_list.append(delete_detail_image_obj)

        # 상품 상세 이미지 업데이트
        ProductImages.objects.bulk_update(update_detail_image_list, ["image"])
        # 상품 상세 이미지 생성
        ProductImages.objects.bulk_create(create_detail_image_list)
        # 상품 상세 이미지 삭제
        [ProductImages(id=delete_image.id).delete()
         for delete_image in delete_detail_image_list]

        # 상품 업데이트
        Product.objects.bulk_update(update_product_obj_list, [
                                    "category", "product_group_name", "product_name", "payment_term", "price", "image", "description"])
        # 상품 생성
        Product.objects.bulk_create(create_product_obj_list)
        # 상품 삭제
        [Product(id=delete_product.id).delete()
         for delete_product in delete_product_obj_list]

        return Response({"detail": "상품이 업데이트 되었습니다."}, status=status.HTTP_200_OK)


