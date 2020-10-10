# from django.contrib import admin
from django.urls import include, path

from apps.client import urls as client_urls

urlpatterns = [
    # Django Admin
    # path('admin/', admin.site.urls),

    # Add your web urls here
    path('', include(client_urls)),
]
