from django.urls import path
from . import views

urlpatterns = [
    path('product/category', views.ProductCategoryListView.as_view(), name="ProductCategoryListView"),
    path('product/list', views.ProductListPaginationViewSet.as_view({'get':'list'}), name='ProductListView'),
    path('product/detail/<int:product_id>', views.ProductDetailView.as_view(), name="ProuctDetailView"),
    path('home', views.HomeView.as_view(), name="HoemView"),
    path('mypage', views.MypageView.as_view(), name='mypageView'),
]