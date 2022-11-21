from django.urls import path
from . import views

urlpatterns = [
    path('api', views.MailView.as_view(), name="mail-api"),
]
