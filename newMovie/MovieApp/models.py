
from django.db import models

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    director = models.CharField(max_length=100, blank=True)
    release_year = models.CharField(max_length=50, blank=True)
    budget = models.CharField(max_length=50, blank=True)
    runtime = models.CharField(max_length=50, blank=True)
    rating = models.CharField(max_length=50, blank=True)
    genre = models.CharField(max_length=50, blank=True)
    image_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)

from django.contrib.auth.models import User

class Role(models.Model):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.rol
