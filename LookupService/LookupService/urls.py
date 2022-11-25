
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('consumer/', include('consumer.urls')),
]

# Add Debug Toolbar
mode = getattr(settings, 'MODE', None)
if mode != 'PRODUCTION':
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
    