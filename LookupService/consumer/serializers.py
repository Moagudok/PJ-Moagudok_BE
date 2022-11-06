from rest_framework import serializers
from sharedb.models import Category

class ProductCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

