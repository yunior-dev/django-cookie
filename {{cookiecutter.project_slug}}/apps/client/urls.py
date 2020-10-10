from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.root_path, name='root_path'),

    # Catch all vue.js routes.
    re_path(r'^.*/$', views.vue_router, name='vue_router'),
]
