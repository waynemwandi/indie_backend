# daraja/urls.py
from django.urls import path
from . import views
from .views import c2b_confirmation

urlpatterns = [
    path('', views.index, name='index'),
    path('c2b_confirmation/', c2b_confirmation, name='c2b_confirmation'),

]
