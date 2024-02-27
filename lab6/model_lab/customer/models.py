from django.db import models
from django.utils import timezone
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places = 2)
    total_items = models.IntegerField()
    order_date= models.DateField(default=timezone.now().date())
