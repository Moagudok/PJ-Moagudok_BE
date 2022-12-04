from rest_framework import serializers
from sharedb.models import Product, ProductImages

class ProductSerializer(serializers.ModelSerializer):
    
    detail_images = serializers.SerializerMethodField()
    
    def get_detail_images(self, obj):
        detail_image_list = []
        image_query = obj.productimages_set.all()
        
        for i in image_query:
            print(i.image)
            detail_image_list.append(i.image)
        return detail_image_list
    
    class Meta:
        model = Product
        fields = "__all__"