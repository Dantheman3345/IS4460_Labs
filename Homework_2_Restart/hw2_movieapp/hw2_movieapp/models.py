from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    image_classpath = models.CharField(max_length=255)
    youtube_link = models.URLField()
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    director = models.CharField(max_length=255)
    release_year = models.IntegerField()
    budget = models.DecimalField(max_digits=14, decimal_places=2)
    runtime = models.IntegerField()
    rating = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MovieTicket(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)  # Or link to your User model
    purchase_date = models.DateField()
    # Add more fields as needed

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roles')
    role = models.CharField(max_length=100)