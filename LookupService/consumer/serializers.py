from rest_framework import serializers
from sharedb.models import Category, Product, User, PaymentTerm, ProductImages

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

# 구독 상품 카드형 정보
class ProductListSerializer(serializers.ModelSerializer):
    payment_term = serializers.SerializerMethodField()

    def get_payment_term(self, obj):
        return obj.payment_term.unit

    class Meta:
        model = Product
        fields = [
            "id", "product_group_name", "subtitle",
            "product_name", "payment_term", "price", "image"
        ]

# 구독 상품 상세 이미지 정보
class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = "__all__"

# 구독 상품 상세 정보
class ProductDetailSerializer(serializers.ModelSerializer):
    productimages = ProductImagesSerializer(many=True, source="productimages_set")
    seller = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    payment_term = serializers.SerializerMethodField()

    def get_seller(self, obj):
        return obj.seller.name

    def get_category(self, obj):
        return obj.category.name

    def get_payment_term(self, obj):
        return obj.payment_term.unit

    class Meta:
        model = Product
        fields = [
            "id", "seller", "category", "product_group_name", "product_name", "subtitle",
            "payment_term", "register_date", "update_date", "price", "image",
            "description", "productimages", "views", "num_of_subscribers",
        ]