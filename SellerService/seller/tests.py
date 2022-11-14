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

    @pytest.mark.skip()
    def test_Read_Product(self, CreateCategories,
                          CreateSignupMethod, CreateUser, CreatePaymentTerm,
                          CreateProductImages, CreateProducts, client):

        url = "/seller/product/1?page=" + \
            str(PAGE_NUM) + "&filter=" + "views" + "&group_name=" + "돼지좋아"

        user1 = User.objects.get(id=1)
        client.force_login(user1)
        resp = client.get(url)

        sellers_products = resp.data['sellers_products']
        total_page = resp.data['total_page']
        is_grouped = resp.data['is_grouped']

        sellers_products_len = len(sellers_products)

        all_product_count = Product.objects.filter(is_active=True).count()

        assert sellers_products_len <= STANDARD_NUM_OF_PRODUCTS
        assert total_page * STANDARD_NUM_OF_PRODUCTS >= all_product_count
        assert sellers_products[0]['views'] >= sellers_products[-1]['views']
        assert is_grouped == True
        assert resp.status_code == 200

    def test_Update_Prodcut(self, CreateCategories,
                            CreateSignupMethod, CreateUser, CreatePaymentTerm,
                            CreateProductImages, CreateProducts, client):

        url = "/seller/product/1/돼지좋아"

        user1 = User.objects.get(id=1)
        client.force_login(user1)

        before_update_price = Product.objects.filter(
            seller=user1, product_group_name="돼지좋아")[0].price
        before_update_detail_images = ProductImages.objects.filter(product=15)[
            0].image

        request_data = {
            "update_product_list" : [{
                "id": 15,
                "category": 1,
                "product_group_name": "업데이트 테스트",
                "product_name": "업데이트 테스트1",
                "payment_term": 3,
                "price": 40000,
                "image": "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff39e8755-f73b-4199-bbd7-a9301a0df299%2FUntitled.png?table=block&id=7c6c3e3b-90d1-429e-b7e9-ef3ece1bab41&spaceId=37dd6269-774e-4741-aba2-448c2fe9ab02&width=2000&userId=b6877bc7-a03e-4708-815c-2ace04f89c71&cache=v2",
                "description": "업데이트용1입니다",
                "detail_images": [
                    'https://simg.ssgcdn.com/trans.ssg?src=/cmpt/edit/202111/16/122021111612425202957885459788_469.jpg&w=830&t=701dd4f9f42c56b83ca9468ecfff9cdfc307df6b',
                    'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg',
                    'https://meattam.com/web/product/tiny/20200604/8081740976679ce5c4c7e6f21eaa4c18.png'
                ],
                "is_active": True
            },
                {
                "id": 16,
                "category": 1,
                "product_group_name": "업데이트 테스트",
                "product_name": "업데이트 테스트2",
                "payment_term": 3,
                "price": 100000,
                "image": "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff39e8755-f73b-4199-bbd7-a9301a0df299%2FUntitled.png?table=block&id=7c6c3e3b-90d1-429e-b7e9-ef3ece1bab41&spaceId=37dd6269-774e-4741-aba2-448c2fe9ab02&width=2000&userId=b6877bc7-a03e-4708-815c-2ace04f89c71&cache=v2",
                "description": "업데이트용2입니다",
                "detail_images": [
                    'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg'
                ],
                "is_active": False
            },
            ],
            "create_product_list" : [{
                "category": 1,
                "product_group_name": "생성테스트",
                "product_name": "생성 테스트1",
                "payment_term": 3,
                "price": 30000,
                "image": "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff39e8755-f73b-4199-bbd7-a9301a0df299%2FUntitled.png?table=block&id=7c6c3e3b-90d1-429e-b7e9-ef3ece1bab41&spaceId=37dd6269-774e-4741-aba2-448c2fe9ab02&width=2000&userId=b6877bc7-a03e-4708-815c-2ace04f89c71&cache=v2",
                "description": "생성용1입니다",
                "detail_images": [
                    'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg',
                    'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg',
                ]},
                {
                "category": 1,
                "product_group_name": "생성테스트",
                "product_name": "생성 테스트2",
                "payment_term": 3,
                "price": 90000,
                "image": "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff39e8755-f73b-4199-bbd7-a9301a0df299%2FUntitled.png?table=block&id=7c6c3e3b-90d1-429e-b7e9-ef3ece1bab41&spaceId=37dd6269-774e-4741-aba2-448c2fe9ab02&width=2000&userId=b6877bc7-a03e-4708-815c-2ace04f89c71&cache=v2",
                "description": "생성용2입니다",
                "detail_images": [
                    'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg',
                    'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg',
                ]}
            ]
        }

        resp = client.put(url, data=json.dumps(
            request_data), content_type="application/json")

        after_update_price = Product.objects.filter(
            seller=user1, product_group_name="업데이트 테스트").first().price
        after_update_detail_images = ProductImages.objects.filter(
            product=15).first().image

        increased_detail_image_count = ProductImages.objects.filter(
            product=15).count()
        decreased_detail_image_count = ProductImages.objects.filter(
            product=16).count()

        create_test_product_count = Product.objects.filter(product_group_name = "생성테스트").count()
        
        assert before_update_price != after_update_price
        assert before_update_detail_images != after_update_detail_images
        assert increased_detail_image_count == 3
        assert decreased_detail_image_count == 1
        assert after_update_price == 40000
        assert Product.objects.get(id=16).is_active == False
        assert create_test_product_count == 2
        assert resp.status_code == 200
