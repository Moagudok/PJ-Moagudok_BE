import json
import pytest

from django.test.client import Client

from rest_framework import status

from sharedb.models import (
    ProductImages,
    Product,
    User)


from seller.views import STANDARD_NUM_OF_PRODUCTS
PAGE_NUM = 1


pytestmark = pytest.mark.django_db


class TestProductView():
    # @pytest.mark.skip()
    def test_Create_Product(self, CreateCategories,
                            CreateSignupMethod, CreateUser,
                            CreatePaymentTerm, client):

        # 상품 등록에 관한 Test
        url = "/seller/product"
        request_data = [{
            "category": 1,
            "product_group_name": "돼지 좋아",
            "product_name": "삼목살",
            "subtitle" : "삼목삼목삼목살입니당",
            "payment_term": 3,
            "price": 30000,
            "image": "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff39e8755-f73b-4199-bbd7-a9301a0df299%2FUntitled.png?table=block&id=7c6c3e3b-90d1-429e-b7e9-ef3ece1bab41&spaceId=37dd6269-774e-4741-aba2-448c2fe9ab02&width=2000&userId=b6877bc7-a03e-4708-815c-2ace04f89c71&cache=v2",
            "description": "삼겹살 300g, 목살 300g",
            "detail_images": [
                'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg',
                'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg',
            ]},
            {
            "category": 1,
            "product_group_name": "소 좋아",
            "product_name": "갈비",
            "subtitle" : "갈비갈비갈비입니당",
            "payment_term": 3,
            "price": 90000,
            "image": "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff39e8755-f73b-4199-bbd7-a9301a0df299%2FUntitled.png?table=block&id=7c6c3e3b-90d1-429e-b7e9-ef3ece1bab41&spaceId=37dd6269-774e-4741-aba2-448c2fe9ab02&width=2000&userId=b6877bc7-a03e-4708-815c-2ace04f89c71&cache=v2",
            "description": "갈비 600g",
            "detail_images": [
                'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg',
                'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg',
            ]},
        ]
        user1 = User.objects.get(id=1)
        client.force_login(user1)
        resp = client.post(url, data=json.dumps(
            request_data), content_type="application/json")
        assert resp.status_code == status.HTTP_201_CREATED

    def test_Update_Prodcut(self, CreateCategories,
                            CreateSignupMethod, CreateUser, CreatePaymentTerm,
                            CreateProductImages, CreateProducts, client):

        url = "/seller/product/1/업데이트 테스트"

        user1 = User.objects.get(id=1)
        client.force_login(user1)

        before_update_price = Product.objects.filter(
            seller=user1, product_group_name="업데이트 테스트")[0].price
        before_update_detail_images = ProductImages.objects.filter(product=11)[
            0].image
        before_total_product_count = Product.objects.count()

        request_data = {
            "update_product_list": [{
                "id": 15,
                "category": 1,
                "product_group_name": "업데이트 테스트",
                "product_name": "업데이트 테스트1",
                "subtitle" : "업데이트 소제목1",
                "payment_term": 3,
                "price": 40000,
                "image": "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff39e8755-f73b-4199-bbd7-a9301a0df299%2FUntitled.png?table=block&id=7c6c3e3b-90d1-429e-b7e9-ef3ece1bab41&spaceId=37dd6269-774e-4741-aba2-448c2fe9ab02&width=2000&userId=b6877bc7-a03e-4708-815c-2ace04f89c71&cache=v2",
                "description": "업데이트용입니다",
            },
                {
                "id": 16,
                "category": 1,
                "product_group_name": "업데이트 테스트",
                "product_name": "업데이트 테스트2",
                "subtitle" : "업데이트 소제목2",
                "payment_term": 3,
                "price": 100000,
                "image": "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff39e8755-f73b-4199-bbd7-a9301a0df299%2FUntitled.png?table=block&id=7c6c3e3b-90d1-429e-b7e9-ef3ece1bab41&spaceId=37dd6269-774e-4741-aba2-448c2fe9ab02&width=2000&userId=b6877bc7-a03e-4708-815c-2ace04f89c71&cache=v2",
                "description": "업데이트용입니다",
            }],
            "create_product_list": [{
                "category": 1,
                "product_group_name": "생성테스트",
                "product_name": "생성 테스트1",
                "subtitle" : "생성 테스트1",
                "payment_term": 3,
                "price": 30000,
                "image": "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff39e8755-f73b-4199-bbd7-a9301a0df299%2FUntitled.png?table=block&id=7c6c3e3b-90d1-429e-b7e9-ef3ece1bab41&spaceId=37dd6269-774e-4741-aba2-448c2fe9ab02&width=2000&userId=b6877bc7-a03e-4708-815c-2ace04f89c71&cache=v2",
                "description": "생성용입니다"
            },
                {
                "category": 1,
                "product_group_name": "생성테스트",
                "product_name": "생성 테스트2",
                "subtitle" : "생성 테스트2",
                "payment_term": 3,
                "price": 90000,
                "image": "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff39e8755-f73b-4199-bbd7-a9301a0df299%2FUntitled.png?table=block&id=7c6c3e3b-90d1-429e-b7e9-ef3ece1bab41&spaceId=37dd6269-774e-4741-aba2-448c2fe9ab02&width=2000&userId=b6877bc7-a03e-4708-815c-2ace04f89c71&cache=v2",
                "description": "생성용입니다"
            }
            ],
            "delete_product_list": [{
                "id": 9
            },
                {
                "id": 10
            }
            ],
            "update_detail_image_list": [{
                "product_id": "12",
                "before_detail_images": [
                    "https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg",
                    "https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail2.jpg",
                ],
                "after_detail_images": [
                    "Changed_image_url1",
                    "Changed_image_url2",
                ]},
                {
                "product_id": "11",
                "before_detail_images": [
                    "https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_it_detail1.jpg",
                    "https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_it_detail2.jpg",
                ],
                "after_detail_images": [
                    "Changed_image_url1",
                    "Changed_image_url2",
                ]}
            ],
            "create_detail_image_list": [{
                "product_id": "15",
                "detail_images": [
                    "https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg",
                    "https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg",
                ]},
                {
                "product_id": "16",
                "detail_images": [
                    "https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg",
                    "https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg",
                ]}
            ],
            "delete_detail_image_list": [{
                "product_id": "15",
                "detail_images": [
                    "https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg",
                    "https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg",
                ]},
                {
                "product_id": "16",
                "detail_images": [
                    "https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg",
                    "https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg",
                ]}
            ]
        }

        resp = client.put(url, data=json.dumps(
            request_data), content_type="application/json")

        after_update_price = Product.objects.filter(
            seller=user1, product_group_name="업데이트 테스트")[0].price
        after_update_detail_images = ProductImages.objects.filter(
            product=11)[0].image

        create_test_product_count = Product.objects.filter(
            description="생성용입니다").count()
        update_test_product_count = Product.objects.filter(
            description="업데이트용입니다").count()
        delete_test_product_count = abs(
            before_total_product_count - create_test_product_count - Product.objects.count())

        assert before_update_price != after_update_price
        assert before_update_detail_images != after_update_detail_images
        assert after_update_price == 40000
        assert create_test_product_count == 2
        assert update_test_product_count == 2
        assert delete_test_product_count == 2
        assert resp.status_code == 200


