from django.shortcuts import render
from django.http import HttpResponse

"""here we are creating views in which we want reposnses"""


def home(request):
    return HttpResponse('home page ')


def products(request):
    return HttpResponse('Products page')


def customer(request):
    return HttpResponse('Customer page')