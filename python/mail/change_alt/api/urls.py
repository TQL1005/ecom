from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.getAPI, name='getAPI'),
    path('post/', views.postAPI, name='postAPI'),
    path('update/<int:pk>', views.putAPI, name='putAPI'),
    path('delete/<int:pk>', views.delAPI, name='delAPI'),
]