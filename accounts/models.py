from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor')
    )
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200,choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    """creating a tuple with drop down Status to choese"""
    STATUS = (
        ('Pending', 'pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'delivered')
    )

    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
