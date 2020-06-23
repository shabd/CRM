from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    # Modified existing url to make it dynamic
    # path('customer/', views.customer),
    path('customer/<str:pk>/', views.customer),

]
