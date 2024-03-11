from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)

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


# New Movie Model
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=500, null=True)
    director = models.CharField(max_length=100, null=True)
    release_year = models.CharField(max_length=50, null=True)
    budget = models.CharField(max_length=50, null=True)
    runtime = models.CharField(max_length=50, null=True)
    rating = models.CharField(max_length=50, null=True)
    genre = models.CharField(max_length=50, null=True)

# New User Model
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, null=True)

# New Role Model
class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=False)
    role = models.CharField(max_length=20, null=False)
