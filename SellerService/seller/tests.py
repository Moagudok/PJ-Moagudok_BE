import json
import pytest

from django.test.client import Client

from rest_framework import status

from sharedb.models import (
    Category,
    PaymentTerm,
    Product,
    User)

pytestmark = pytest.mark.django_db


class TestProductView():
    
    def test_상품_등록(self, CreateCategories, \
        CreateSignupMethod, CreateUser, CreatePaymentTerm, \
        CreateProductImages, CreateProducts, client):
        url = "/seller/product"
        request_data ={
            "category" : 1,
            "product_group_name" : "돼지 좋아",
            "product_name" : "삼목살",
            "payment_term" : 3,
            "price" : 30000,
            "image" : "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff39e8755-f73b-4199-bbd7-a9301a0df299%2FUntitled.png?table=block&id=7c6c3e3b-90d1-429e-b7e9-ef3ece1bab41&spaceId=37dd6269-774e-4741-aba2-448c2fe9ab02&width=2000&userId=b6877bc7-a03e-4708-815c-2ace04f89c71&cache=v2",
            "description" : "삼겹살 300g, 목살 300g",
            "detail_images" : [
                'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg',
                'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg',
                ]
            }
        client = Client()
        user1 = User.objects.get(id=1)
        client.force_login(user1)
        resp = client.post(url, data=json.dumps(request_data), content_type="application/json")
        assert resp.status_code == status.HTTP_201_CREATED