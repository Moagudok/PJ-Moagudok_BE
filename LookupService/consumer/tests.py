import pytest
from sharedb.models import Category

'''
카테고리 리스트 조회 화면 TESTCODE
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

'''
상품 리스트 조회 (by 카테고리) 화면 TESTCODE
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


'''
상품 리스트 조회 (by 텍스트) 화면 TESTCODE
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