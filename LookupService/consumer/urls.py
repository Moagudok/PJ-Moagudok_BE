from django.urls import path
from . import views

urlpatterns = [
    path('product/list', views.ProductListPaginationViewSet.as_view({'get':'list'}), name='ProductListView'),
    path('product/cursor/list', views.ProductListCursorPaginationViewSet.as_view({'get':'list'}), name='ProductListCursorView'),
    path('product/detail/<int:product_id>', views.ProductDetailView.as_view(), name="ProuctDetailView"),
    path('product/subscriber', views.ManageSubscriber.as_view(), name='ManageSubscriberView'),
    path('home', views.HomeView.as_view(), name="HoemView"),
    path('mypage', views.MypageView.as_view(), name='mypageView'),
]