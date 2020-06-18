from django.shortcuts import render
from django.http import HttpResponse

""" Istead of using HTTP Response and passing a sting as a reposne 
we use RENDER , which looks for the html templates we created to display the pages """


def home(request):
    return render(request, 'accounts/dashboard.html')


def products(request):
    return render(request, 'accounts/products.html')


def customer(request):
    return render(request, 'accounts/customer.html')
