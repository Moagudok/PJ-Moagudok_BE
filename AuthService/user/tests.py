import pytest
from sharedb.models import Category, ProductImages, Product, User, SignupMethod, PaymentTerm

class TestSignUp():
    # 회원가입 TEST
    
    def test_create_user(self):
        user = User(
            name = "test",
            email = "test@test.com",
            password = "!asdfg",
            address = "부산 쌍둥이마을",
        )