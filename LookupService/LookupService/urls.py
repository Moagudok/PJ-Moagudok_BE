
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('consumer/', include('consumer.urls')),
]

# Add Debug Toolbar
mode = getattr(settings, 'MODE', None)
if mode != 'PRODUCTION':
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
    