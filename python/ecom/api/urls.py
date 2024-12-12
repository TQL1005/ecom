from django.urls import path
from . import views

urlpatterns = [
    path('customer',views.Customer,name='customer'),
    path('product',views.Product,name='product'),
    path('order_item',views.Order_item,name='order_item'),
]