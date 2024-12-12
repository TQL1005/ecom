from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name='main_view'),
    path('cart/',views.cart,name='cart'),
]