from django.urls import path
from . import views

urlpatterns = [
    path('latest', views.SearchLatestTextListView.as_view(), name="SearchLatestTextListView"),
    path('tophits', views.SearchTopHitTextListView.as_view(), name="SearchTopHitTextListView"),
]