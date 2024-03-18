from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/', null=True)
    notes = models.TextField(null=True)
    linkedin = models.URLField(null=True)
    STATUS_CHOICES = [
        ('new', 'New'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('closed', 'Closed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return self.name
    


    
class Order(models.Model):

    customer = models.ForeignKey(to = Customer,on_delete = models.CASCADE)
    order_total = models.DecimalField(max_digits=7,decimal_places=2)
    notes = models.CharField(max_length=100,default='')

    status_choices = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed')
    )

    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default='pending'
    )


class Contact(models.Model):
    customer = models.ForeignKey(to = Customer,on_delete = models.CASCADE)
    phone = models.CharField(max_length = 17)
    email = models.EmailField()


