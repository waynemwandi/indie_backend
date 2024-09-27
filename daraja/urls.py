# daraja/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test-api/", views.test_api, name="test_api"),
    path("payments/", views.get_payments, name="get_payments"),
    path("c2b_confirmation/", views.c2b_confirmation, name="c2b_confirmation"),
    path("c2b_validation/", views.c2b_validation, name="c2b_validation"),
    path("register/", views.register_urls, name="register_urls"),
    path("test_access_token/", views.test_access_token, name="test_access_token"),
]
