from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<slug:id>/search', initialization, name='search'),
    re_path(r'^old/(?P<year>[0-9]{4})/', archive, name='archive'),
]