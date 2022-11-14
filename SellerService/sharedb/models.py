from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

SIGNUP_METHOD = (
        ("Standard", "홈페이지"), ("Google", "구글"),
)    

UNIT_CHOICES = (
    ("day", "일"), ("week", "주"), ("month", "월"), ("quarter", "분기"),
)

# 가입 방법 Table
class SignupMethod(models.Model):
    method = models.CharField("가입 방법", choices = SIGNUP_METHOD, max_length=10) # google, basic
    
    class Meta:
        db_table = 'SignupMethod'


class UserManager(BaseUserManager):
    #일반 유저 생성
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('must have an email')
        user = self.model(
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # 관리자 계정 생성
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# User(소비자/판매자) Table
class User(AbstractBaseUser):        
    email = models.EmailField("이메일", max_length=150, unique=True, null=False, blank=False)
    name = models.CharField("이름", max_length=20)
    password = models.CharField("비밀번호", max_length=100)
    address = models.CharField("주소", max_length=100)
    join_date = models.DateTimeField("가입일", auto_now_add=True)
    signup_method = models.ForeignKey(SignupMethod, verbose_name="가입방법", on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True) # 계정활성화 여부
    is_seller = models.BooleanField(default=False) # 판매자 여부
    USERNAME_FIELD = 'email' # 로그인 시 사용할 필드 지정

    objects = UserManager() # custom user 생성 시 필요

    class Meta:
        db_table = 'User'

# 카테고리
class Category(models.Model):
    name = models.CharField("카테고리 이름", max_length=30)
    image = models.TextField("카테고리 대표 이미지", null=True, blank=True)
    
    class Meta:
        db_table = 'Category'

# 결제 주기
class PaymentTerm(models.Model):
    unit = models.CharField("분기 유형", max_length=100, choices=UNIT_CHOICES)
    
    class Meta:
        db_table = 'PaymentTerm'

# 상품
class Product(models.Model):
    seller = models.ForeignKey(User, verbose_name = "판매자 ID", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    product_group_name = models.CharField("상품 그룹명", max_length=30)
    product_name = models.CharField("상품명", max_length=30)
    payment_term = models.ForeignKey(PaymentTerm, verbose_name = "구독 기간 단위", on_delete=models.SET_NULL, null=True) 
    register_date = models.DateField("상품 최초 등록일", auto_now_add=True) 
    update_date = models.DateField("상품 수정일", auto_now=True)
    price = models.PositiveIntegerField("상품 가격")
    image = models.TextField("상품 대표 이미지", null=True, blank=True)
    description = models.TextField("상품 설명")
    views = models.PositiveIntegerField("상품 조회 수", default=0)
    num_of_subscribers = models.PositiveIntegerField("구독자 수", default=0)
    is_active = models.BooleanField("활성화 여부", default=True)
    
    class Meta:
        db_table = 'Product'


# 상품 상세 이미지들
class ProductImages(models.Model):
    image = models.TextField("상품 상세 이미지", null=True, blank=True)
    product = models.ForeignKey(Product, verbose_name="소속 상품", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'ProductImages'

# 결제 정보 (=구독 정보)
class Payment(models.Model):
    consumer = models.ForeignKey(User, related_name = 'consumer', verbose_name = "소비자ID", on_delete=models.SET_NULL , null=True)
    seller = models.ForeignKey(User, related_name = 'seller', verbose_name = "판매자ID", on_delete=models.SET_NULL , null=True)
    product = models.ForeignKey(Product, verbose_name = "상품ID", on_delete=models.SET_NULL , null=True)
    price = models.PositiveIntegerField("상품 가격")
    subscription_date = models.DateField("구독시작일", auto_now=True)
    expiration_date = models.DateField("만료예정일", auto_now=True)
    payment_due_date = models.DateField("결제예정일", auto_now=True)
    
    class Meta:
        db_table = 'Payment'