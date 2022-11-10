from django.urls import path
from . import views

urlpatterns = [
    path('product', views.ProductView.as_view(), name="product"),
]
