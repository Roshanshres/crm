from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null = True)
    phone = models.CharField(max_length=200, null = True)
    email = models.CharField(max_length=200, null = True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 200, null = True)
    price= models.CharField(max_length = 200, null = True)
    category = models.CharField(max_length = 200, null = True)
    description = models.CharField(max_length = 200, null = True)
    date_created = models.DateField(auto_now_add=True, null= True)

class Order(models.Model):