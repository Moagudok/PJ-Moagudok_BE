
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('consumer/', include('consumer.urls')),
    path('search/', include('search.urls')),
]
