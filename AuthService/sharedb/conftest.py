import pytest
from sharedb.models import Category, ProductImages, Product, User, SignupMethod, PaymentTerm

@pytest.fixture
def CreateSignupMethod():
    SignupMethod.objects.bulk_create([
        SignupMethod(1, 'basic'),
        SignupMethod(2, 'google'),
    ])
    print("SignupMethod is created")