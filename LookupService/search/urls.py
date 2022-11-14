from django.urls import path
from . import views

urlpatterns = [
    path('latest', views.SearchLatestTextListView.as_view(), name="SearchLatestTextListView"),
]