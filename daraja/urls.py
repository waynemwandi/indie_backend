# daraja/urls.py
from django.urls import path

from . import views
from .views import c2b_confirmation, test_api

urlpatterns = [
    path("", views.index, name="index"),
    path("c2b_confirmation/", c2b_confirmation, name="c2b_confirmation"),
    path("test-api/", test_api, name="test_api"),
    path("payments/", views.get_payments, name="get_payments"),
]
