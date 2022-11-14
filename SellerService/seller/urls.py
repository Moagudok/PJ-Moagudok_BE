from django.urls import path
from . import views

urlpatterns = [
    path('product', views.ProductView.as_view(), name="product"),
    path('product/<int:seller_id>', views.ProductView.as_view(), name="product_seller"),
    path('product/<int:seller_id>/<str:group_name>', views.ProductView.as_view(), name="product_seller"),
]
