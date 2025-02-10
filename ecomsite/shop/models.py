from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()                         # can fit more data and more text thabn CharField()
    image = models.CharField(max_length=300)



class Order(models.Model):
    items = models.CharField(max_length=1000)
    name1 = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    address1 = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)





