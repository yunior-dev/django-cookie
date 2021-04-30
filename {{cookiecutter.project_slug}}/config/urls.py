from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # API urls: Make changes to backend in api.py
    path('api/', include('urls.api')),

    # Web urls: Make changes to frontend in web.py
    path('', include('urls.web')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
