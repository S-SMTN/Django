from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    path('<slug:id>/search', initialization),
    re_path(r'^old/(?P<year>[0-9]{4})/', archive),
]