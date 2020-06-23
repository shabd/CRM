from django.shortcuts import render
from django.http import HttpResponse
from .models import *

""" Instead of using HTTP Response and passing a string as a reponse 
we use RENDER , which looks for the html templates we created to display the pages """


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    """instead of passing the dictionary in the return  statment we creating 
    a dictionary outside and pass it inside """

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request, pk):
    # We Want to make our customer url dynamic -- meaning
    # we have a separate page for each user.
    # create a dynamic customer view and url
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)
