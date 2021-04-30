from django.urls import {%+ if cookiecutter.use_vuejs == "y" %}include,{%+ endif %} path
{%+ if cookiecutter.use_vuejs == "n" %}
# Delete - this is for presentation only.
# Your views should be in a views.py file.
from django.shortcuts import render  # isort:skip


def welcome(request):  # Delete - this is for presentation only.
    return render(request, 'welcome.html')
{%+ endif %}

urlpatterns = [
    {%- if cookiecutter.use_vuejs == "y" %}
    # Add your web urls here
    path('', include('client.urls')),
    {%- elif cookiecutter.use_vuejs == "n" %}
    # Add your web urls here
    path('', welcome),
    {%- endif %}
]
