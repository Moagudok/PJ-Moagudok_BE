from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:seller_id>', views.ProductView.as_view(), name="product_seller"),
    path('product/dashboard/sales-info/<int:year>/<int:month>', views.DashBoardSalesInfoView.as_view(), name="dashboard_sales_info"),
    path('product/dashboard/customer-info', views.DashBoardCustomerINfoView.as_view(), name="dashboard_customer_info"),
]
