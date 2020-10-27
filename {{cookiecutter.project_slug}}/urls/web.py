from django.urls import include, path

urlpatterns = [
    # Add your web urls here
    path('', include('client.urls')),
]
