from django.urls import path
from . import views

urlpatterns = [
    path('product/category/', views.ProductCategoryListView.as_view(), name="ProductCategoryListView"),
    path('product/list', views.ProductListPaginationViewSet.as_view({'get':'list'}), name='ProductListView'),
    path('product/detail/<int:product_id>', views.ProductDeatilView.as_view(), name="ProuctDetailView"),
]