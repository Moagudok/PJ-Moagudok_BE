from rest_framework import serializers
from sharedb.models import Category, Product

class ProductCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
