from django.conf import settings
from django.urls import include, path

urlpatterns = [
    # API urls: Make changes to backend in api.py
    path('api/', include('urls.api')),

    # Web urls: Make changes to frontend in web.py
    path('', include('urls.web')),
]

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar  # isort:skip

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls))
        ] + urlpatterns
