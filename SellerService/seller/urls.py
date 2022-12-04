from django.urls import path
from . import views

urlpatterns = [
    path('product', views.ProductView.as_view(), name="product"),
    path('product/<str:group_name>', views.ProductView.as_view(), name="product_seller"),
]
