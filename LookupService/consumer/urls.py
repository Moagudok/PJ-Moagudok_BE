from django.urls import path
from . import views

urlpatterns = [
    path('product/category/', views.ProductCategoryListView.as_view(), name="ProductCategoryListView"),
]