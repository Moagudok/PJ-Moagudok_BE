import pytest
from sharedb.models import Category, ProductImages, Product, User, SignupMethod, PaymentTerm

'''
카테고리 리스트 조회 화면 TESTCODE
'''
@pytest.mark.skip()
# @pytest.mark.django_db
class TestCategory():
    ## 결함 TEST 
    # - Category 값 중 누락된건 없는지
    # - 모든 Rows에 name과 image값이 다 있는지
    def test_CategoryRowsValidation(self, CreateCategories):
        queryset = list(Category.objects.all())
        assert len(queryset)==12, "Num of Category Rows is Failed"
        assert all([obj.name for obj in queryset if obj.name is not None]) # 모두 True면 통과
        assert all([obj.image for obj in queryset if obj.image is not None]) # 모두 True면 통과

    ## DB ListView 반환 Test
    # - 갯수가 맞는지, 상태코드 체크
    def test_CategoryList(self, CreateCategories, client):
        resp = client.get("/consumer/product/category/")
        obj_cnt = Category.objects.count()
        assert obj_cnt == 12, "Num of Category Rows is Failed"
        assert resp.status_code == 200

'''
상품 리스트 조회 (by 카테고리) 화면 TESTCODE
'''
# @pytest.mark.skip()
@pytest.mark.django_db
class TestProductList():
    # DB ListView 반환 Test
    # - 갯수와 예외 처리에 대한 status 검사
    @pytest.mark.django_db
    def test_ProductListbyCategory(self, CreateCategories, \
        CreateSignupMethod, CreateUser, CreatePaymentTerm, \
        CreateProducts, CreateProductImages, client):
        resp = client.get("/consumer/product/list?category=1")
        assert len(resp.data) >= 0
        assert resp.status_code == 200
        
        resp = client.get("/consumer/product/list?category=500")
        assert resp.data['message'] == 'There are no products in this category'
        assert resp.status_code == 200

        resp = client.get("/consumer/product/list?category=abc")
        assert resp.data['message'] == 'Params is invalid'
        assert resp.status_code == 400