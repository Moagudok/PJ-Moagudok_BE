from rest_framework import status, exceptions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from sharedb.models import Product, ProductImages

from .serializers import ProductSerializer


class ProductView(APIView):

    def post(self, request: Request) -> Response:
        try:
                
            request.data["seller"] = self.request.user.id
            create_product_serializer = ProductSerializer(data=request.data)
            create_product_serializer.is_valid(raise_exception=True)
            create_product_serializer.save()
            
            detail_images = request.data.pop("detail_images")
            detail_images_list = [ProductImages(image = image ,product = create_product_serializer.instance ) for image in detail_images]
            ProductImages.objects.bulk_create(detail_images_list)
            
            return Response({"detail": "상품이 등록 되었습니다."}, status=status.HTTP_201_CREATED)
        except exceptions.ValidationError as e:
                error_message = "".join([str(value) for values in e.detail.values() for value in values])
                return Response({"detail": error_message}, status=status.HTTP_400_BAD_REQUEST)