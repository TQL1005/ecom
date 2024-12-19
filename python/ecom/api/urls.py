from django.urls import path
from . import views

urlpatterns = [
    path('customer',views.Customer,name='customer'),
    path('product',views.Product,name='product'),
    path('order_item',views.Order_item,name='order_item'),
    path('order_item_update',views.Order_item_update,name='order_item_update'),
    path('process_order',views.process_order,name='process_order'),
]