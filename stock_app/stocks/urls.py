from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_stock, name='add_stock'),
    path('list/', views.stock_list, name='stock_list'),
]
