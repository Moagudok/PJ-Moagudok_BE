import pytest
from sharedb.models import Category

@pytest.fixture
def CreateCategories():
    Category.objects.bulk_create([
        Category(1, 'coffee', 'https://www.notion.so/b1181e58e1c947739b2022dcfed9e6c8#44662a62706046858c1f3e3cb504aaef'),
        Category(2, 'meat', 'https://www.notion.so/b1181e58e1c947739b2022dcfed9e6c8#d9cfdc4c419f4fb18ec880e162ff7a6a'),
        Category(3, 'crawling', 'https://www.notion.so/b1181e58e1c947739b2022dcfed9e6c8#ef93029e30e440f1974a769890b4a1a3'),
        Category(4, 'munchies', 'https://www.notion.so/b1181e58e1c947739b2022dcfed9e6c8#e7662ac3dcd34d2a9d8927d360c2bee4')
    ])
    print("Create Category-rows is succeed")

# 결함 TEST
# 1. Category 값 중 누락된건 없는지
# - 모든 Rows에 name과 image값이 다 있는지
# @pytest.mark.skip()
@pytest.mark.django_db
def test_CategoryRowsValidation(CreateCategories):
    queryset = list(Category.objects.all())
    assert len(queryset)==4, "Num of Category Rows is Failed"
    assert all([obj.name for obj in queryset if obj.name is not None]) # 모두 True면 통과
    assert all([obj.image for obj in queryset if obj.image is not None]) # 모두 True면 통과

# DB ListView 반환 Test
# - 갯수가 맞는지, 상태코드 체크
@pytest.mark.django_db
def test_CategoryList(CreateCategories, client):
    resp = client.get("/consumer/product/category/")
    obj_cnt = Category.objects.count()
    assert obj_cnt == 4
    assert resp.status_code == 200

    