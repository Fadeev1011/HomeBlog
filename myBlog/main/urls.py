from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
import debug_toolbar


from .views import *

urlpatterns = [
    path('test/', test_dashboard_index, name='test'),
]



if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)