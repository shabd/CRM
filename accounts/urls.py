from django.urls import path

from . import views

urlpatterns = [
    # making the links more dynamic by adding name field
    path('', views.home, name='home'),
    path('products/', views.products, name='product'),
    path('customer/<str:pk>/', views.customer, name='customer'),

]
