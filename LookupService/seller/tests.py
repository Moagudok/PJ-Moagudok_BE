import pytest

from django.test.client import Client


from sharedb.models import (
    Product,
    User)


from seller.views import STANDARD_NUM_OF_PRODUCTS
PAGE_NUM = 1


pytestmark = pytest.mark.django_db


class TestProductView():
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

        all_product_count = Product.objects.all().count()

        assert sellers_products_len <= STANDARD_NUM_OF_PRODUCTS
        assert total_page * STANDARD_NUM_OF_PRODUCTS >= all_product_count
        assert sellers_products[0]['views'] >= sellers_products[-1]['views']
        assert is_grouped == True
        assert resp.status_code == 200
        
class TestDashBoardSalesInfoView():
    def test_get_dashboard_sales_info(self, CreateCategories,
                            CreateSignupMethod, CreateUser, CreatePaymentTerm,
                            CreateProductImages, CreateProducts, client):
        
        
        url = "/seller/product/dashboard/sales-info"
        
        
        # user1 = User.objects.get(id=seller_id)
        user1 = User.objects.get(id=1)
        client.force_login(user1)
        resp = client.get(url)
        
        daily_sales_dict = resp.data["daily_sales_dict"]
        this_year_total_sales = resp.data["this_year_total_sales"]
        
        assert resp.status_code == 200
        
        
class TestDashBoardCustomerINfoView():
    def test_get_dashboard_customer_info(self, CreateCategories,
                            CreateSignupMethod, CreateUser, CreatePaymentTerm,
                            CreateProductImages, CreateProducts, client):
        
        url = "/seller/product/dashboard/customer-info"
        
        user1 = User.objects.get(id=1)
        client.force_login(user1)
        resp = client.get(url)
        
        total_percent = 0
        for product in resp.data["query_count_list"]:
            total_percent += product["subscribe_percent"]
        
        assert resp.status_code == 200
        assert 99 <= total_percent <= 100
