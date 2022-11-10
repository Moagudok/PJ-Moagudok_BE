from rest_framework import serializers
from sharedb.models import Product

class ProductSerializer(serializers.ModelSerializer):
    
        
    class Meta:
        model = Product
        fields = "__all__"