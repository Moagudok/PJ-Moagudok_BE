import pytest
from sharedb.models import Category, ProductImages, Product, User, SignupMethod, PaymentTerm


@pytest.fixture
def CreateCategories():
    Category.objects.bulk_create([
        Category(
            1, 'IT 서비스', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_it_service.jpg'),
        Category(
            2, '육류', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_meat.jpg'),
        Category(
            3, '가공식품', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_processed_food.jpg'),
        Category(
            4, '커피 및 음료', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_coffee.jpg'),
        Category(
            5, '주류', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_alcohol.jpg'),
        Category(
            6, '도시락', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_luch_box.jpg'),
        Category(
            7, '샐러드', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_salad.jpg'),
        Category(8, '채소 및 과일', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_vegetables_fruits.jpg'),
        Category(
            9, '유제품', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_dairy_product.jpg'),
        Category(
            10, '식물', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_plant.jpg'),
        Category(
            11, '안주', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_munchies.jpg'),
        Category(
            12, '가전제품', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_appliances.jpg')
    ])
    print("Categories is created")


@pytest.fixture
def CreateSignupMethod():
    SignupMethod.objects.bulk_create([
        SignupMethod(1, 'basic'),
        SignupMethod(2, 'google'),
    ])
    print("SignupMethod is created")


@pytest.fixture
def CreateUser():
    User.objects.bulk_create([
        User(1, None, 'khw7876@naver.com', "고현우",
             "pbkdf2_sha256$320000$vf66x5jmyVDASF8jq3wxni$sGbiGS0AEuC1xHgttw/EbSirrBAnbiOZtmvA+RV/zWE=",
             "경기 수원", "2022-11-08 08:12:14", True, True, 1),
    ])
    print("User is created")


@pytest.fixture
def CreatePaymentTerm():
    PaymentTerm.objects.bulk_create([
        PaymentTerm(1, '일'),
        PaymentTerm(2, '주'),
        PaymentTerm(3, '월'),
        PaymentTerm(4, '분기'),
    ])
    print("PaymentTerm is created")


@pytest.fixture
def CreateProductImages():
    ProductImages.objects.bulk_create([
        ProductImages(
            11, 'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg', 12),
        ProductImages(
            12, 'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail2.jpg', 12),
        ProductImages(
            13, 'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_it_detail1.jpg', 11),
        ProductImages(
            14, 'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_it_detail2.jpg', 11),
        ProductImages(
            15, 'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_processed_food_spam_detail1.jpg', 17),
        ProductImages(
            16, 'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_processed_food_tuna_detail1.jpg', 18),
    ])
    print("ProductImages is created")


@pytest.fixture
def CreateProducts():
    Product.objects.bulk_create([
        Product(11, 1, 1, '뉴스 크롤링', 'IT TOP 10', 2, '2022-11-07', '2022-11-07', 10000,
                'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_it.jpg', '주간 IT 헤드라인 TOP 10 뉴스 크롤링하여 전달해드립니다.',
                5, 2),
        Product(12, 1, 1, '뉴스 크롤링', '정치 TOP 10', 1, '2022-11-08', '2022-11-08', 10000,
                'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics.jpg', '일일 정치 헤드라인 TOP 10 뉴스 크롤링하여 전달해드립니다.',
                10, 0),
        Product(13, 1, 1, '증권 주가 통계 정보', '식량관련주', 1, '2022-11-06', '2022-11-06', 5000,
                'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_stock_food.jpg', '일일 식량관련주 통계 분석 하여 제공해드립니다.',
                35, 1),
        Product(14, 1, 1, '증권 주가 통계 정보', '엔터관련주', 3, '2022-11-08', '2022-11-08', 5000,
                'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_stock_entertainment.jpg', '월간 엔터관련주 통계 분석 하여 제공해드립니다.',
                77, 98),
        Product(15, 1, 2, '돼지좋아', '삼목살', 2, '2022-11-05', '2022-11-06', 30000,
                'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_meat_porkbelly.jpg', '삼겹살 300g과 목살 300g 조합의 고기셋트',
                15, 42),
        Product(16, 1, 2, '돼지좋아', '등심럽', 2, '2022-11-03', '2022-11-04', 40000,
                'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_meat_sirloinjpg.jpg', '등심 600g 조합의 고기셋트',
                13, 7),
        Product(17, 1, 3, '통조림가공식품', '스팸셋트', 3, '2022-11-03', '2022-11-04', 25000,
                'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_processed_food_spam.jpg', '스팸에 쌀밥 먹고 싶은 사람만~',
                31, 4),
        Product(18, 1, 3, '통조림가공식품', '참치셋트', 3, '2022-11-05', '2022-11-08', 15000,
                'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_processed_food_tuna.jpg', '참치 통조림 다양하게 먹고 싶은 사람만~',
                22, 5),
    ])
    print("Product is created")
