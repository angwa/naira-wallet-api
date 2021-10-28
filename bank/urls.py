from os import name
from django.urls import path
from . import views 

urlpatterns = [
    path('create', views.Bank.as_view(), name='create_bank'),
    path('list', views.Bank.as_view(), name='list_banks'),
]