from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length = 15)
# Create your models here.



class Order(models.Model):
    title = models.CharField(max_length=255, default='Default Title')
    description = models.CharField(max_length=255,default='Default Description')
    status = models.CharField(max_length=255, default='pending')