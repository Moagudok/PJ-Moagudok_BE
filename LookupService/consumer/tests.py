import pytest
from sharedb.models import Category, Product
from rest_framework.exceptions import ErrorDetail

''' 카테고리 리스트 조회 화면 TESTCODE
결함 TEST 위주
- Category 값 중 누락된건 없는지
- 모든 Rows에 name과 image값이 다 있는지
'''
@pytest.mark.skip()
# @pytest.mark.django_db
class TestCategory():
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

''' 상품 리스트 조회 (by 카테고리) 화면 TESTCODE
- 페이지 별 항목(row) 갯수가 맞는지
- 첫 페이지 항목 속성 검사, 상태코드 검사
- 모든 페이지가 정상적으로 다 반환되는지 (속성, 상태코드)
- 페이지 초과하는 경우
'''
@pytest.mark.skip()
# @pytest.mark.django_db
class TestProductListbyCategory():
    @pytest.mark.skip()
    def test_ProductListbyCategory(self, CreateCategories, \
        CreateSignupMethod, CreateUser, CreatePaymentTerm, \
        CreateProducts, CreateProductImages, client):
        PAGE_SIZE = 2
        resp = client.get("/consumer/product/list?category=1&search&page=1")
        assert len(resp.data['results']) == PAGE_SIZE
        assert resp.data['previous'] == None
        assert resp.status_code == 200

        # 마지막 page 번호 구하기
        PAGE_COUNT = resp.data['count'] // PAGE_SIZE
        if resp.data['count'] % PAGE_SIZE != 0:
            PAGE_COUNT+=1

        # 통과 갯수 - 모든 Request 가 잘 들어왔는지
        pass_count = 0
        for i in range(1, PAGE_COUNT+1):
            resp = client.get("/consumer/product/list?category=1&search&page="+str(i)) 
            assert len(resp.data['results']) == PAGE_SIZE
            assert resp.status_code == 200
            pass_count+=1
        assert pass_count == PAGE_COUNT

        # Page 초과시
        resp = client.get("/consumer/product/list?category&search=top&page="+str(PAGE_COUNT+1))
        assert resp.status_code == 404
        assert resp.data['detail'].code == 'not_found' # from rest_framework.exceptions import ErrorDetail


''' 상품 리스트 조회 (by 텍스트) 화면 TESTCODE
- 페이지 별 항목(row) 갯수가 맞는지
- 첫 페이지 항목 속성 검사, 상태코드 검사
- 모든 페이지가 정상적으로 다 반환되는지 (속성, 상태코드)
- 페이지 초과하는 경우
'''
@pytest.mark.skip()
# @pytest.mark.django_db
class TestProductListbyText():
    @pytest.mark.skip()
    def test_ProductListbySearchText(self, CreateCategories, \
        CreateSignupMethod, CreateUser, CreatePaymentTerm, \
        CreateProducts, CreateProductImages, client):
        PAGE_SIZE = 2
        resp = client.get("/consumer/product/list?category&search=top&page=1")
        assert len(resp.data['results']) == PAGE_SIZE
        assert resp.data['previous'] == None
        assert resp.status_code == 200

        # 마지막 page 번호 구하기
        PAGE_COUNT = resp.data['count'] // PAGE_SIZE
        if resp.data['count'] % PAGE_SIZE != 0:
            PAGE_COUNT+=1

        # 통과 갯수 - 모든 Request 가 잘 들어왔는지
        pass_count = 0
        for i in range(1, PAGE_COUNT+1):
            resp = client.get("/consumer/product/list?category&search=top&page="+str(i)) 
            assert len(resp.data['results']) == PAGE_SIZE
            assert resp.status_code == 200
            pass_count+=1
        assert pass_count == PAGE_COUNT

        # page 초과시
        resp = client.get("/consumer/product/list?category&search=top&page="+str(PAGE_COUNT+1))
        assert resp.status_code == 404
        assert resp.data['detail'].code == 'not_found' # from rest_framework.exceptions import ErrorDetail



''' 상품 상세 화면 TESTCODE
- 총 상품 갯수 넘을 때 - 404
- 총 상품 갯수 안넘을 때 - 200
'''
@pytest.mark.skip()
# @pytest.mark.django_db
class TestProductDetail():
    def test_ProductDetail(self, CreateCategories, \
        CreateSignupMethod, CreateUser, CreatePaymentTerm, \
        CreateProducts, CreateProductImages, client):
        
        product_num = Product.objects.count()
        resp = client.get("/consumer/product/detail/"+str(product_num))
        assert resp.status_code == 200

        resp = client.get("/consumer/product/detail/"+str(product_num+1))
        assert resp.data == ErrorDetail(string = '존재하지 않는 구독 상품 입니다.', code=404)
        assert resp.status_code == 404
        
''' 홈 화면 TESTCODE - 1
- 카테고리 모두 조회됬는지
'''
# @pytest.mark.django_db
@pytest.mark.skip()
class TestHomeCategory():
    # 카테고리 TEST
    def test_HomeCategoryList(self, CreateCategories, client):
        resp = client.get("/consumer/home/")
        assert len(resp.data['categories'])==12, "Num of Category is invalid"
        assert resp.status_code == 200

''' 홈 화면 TESTCODE - 2
- 인기 상품 : 10개 넘을 때, 10개 안넘을 떄 다 잘 출력되는지
- 인기 상품 : 상품 리스트 중 앞 상품 구독자가 뒤 상품 구독자보다 많은지 
'''
# @pytest.mark.django_db
@pytest.mark.skip()
class TestHomePopularProducts():
    # 인기 상품 TEST - 상품 갯수 많은
    def test_HomePopularProductList(self, CreateCategories, \
        CreateSignupMethod, CreateUser, CreatePaymentTerm, \
        CreateProducts, CreateProductImages, client):

        STANDARD_NUM_OF_PRODUCTS = 10 # 기본 제공 상품 갯수

        resp = client.get("/consumer/home/")
        popular_products = resp.data['popular_products']
        popular_products_len = len(popular_products)
        assert popular_products_len >= STANDARD_NUM_OF_PRODUCTS
        assert popular_products[0]['num_of_subscribers'] >= popular_products[popular_products_len-1]['num_of_subscribers']
        assert resp.status_code == 200

    # @pytest.mark.skip()
    # 인기 상품 TEST - 상품 갯수 적은
    def test_HomePopularProductSmallList(self, CreateCategories, \
        CreateSignupMethod, CreateUser, CreatePaymentTerm, \
        CreateSmallProducts, CreateSmallProductImages, client):

        STANDARD_NUM_OF_PRODUCTS = 10 # 기본 제공 상품 갯수

        resp = client.get("/consumer/home/")
        popular_products = resp.data['popular_products']
        popular_products_len = len(popular_products)
        assert popular_products_len < STANDARD_NUM_OF_PRODUCTS
        assert popular_products[0]['num_of_subscribers'] >= popular_products[popular_products_len-1]['num_of_subscribers']
        assert resp.status_code == 200

''' 홈 화면 TESTCODE - 3
- 신규 상품 : UPDATE 날짜가 빠른 10개 상품 출력
'''
# @pytest.mark.django_db
@pytest.mark.skip()
class TestHomePopularProduct():
    # 신규 상품 TEST - 상품 갯수 많은 
    def test_HomeNewProductList(self, CreateCategories, \
        CreateSignupMethod, CreateUser, CreatePaymentTerm, \
        CreateProducts, CreateProductImages, client):

        STANDARD_NUM_OF_PRODUCTS = 10 # 기본 제공 상품 갯수

        resp = client.get("/consumer/home/")
        new_products = resp.data['new_products']
        new_products_len = len(new_products)
        assert new_products_len >= STANDARD_NUM_OF_PRODUCTS
        assert new_products[0]['update_date'] >= new_products[new_products_len-1]['update_date'] # '2022-11-09' > '2022-11-08' = True
        assert resp.status_code == 200

    # 신규 상품 TEST - 상품 갯수 적은 
    def test_HomeNewProductSmallList(self, CreateCategories, \
        CreateSignupMethod, CreateUser, CreatePaymentTerm, \
        CreateSmallProducts, CreateSmallProductImages, client):

        STANDARD_NUM_OF_PRODUCTS = 10 # 기본 제공 상품 갯수

        resp = client.get("/consumer/home/")
        new_products = resp.data['new_products']
        new_products_len = len(new_products)
        assert new_products_len < STANDARD_NUM_OF_PRODUCTS
        assert new_products[0]['update_date'] >= new_products[new_products_len-1]['update_date'] # '2022-11-09' > '2022-11-08' = True
        assert resp.status_code == 200
        
