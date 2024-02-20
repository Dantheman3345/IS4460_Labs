from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    image_classpath = models.CharField(max_length=255)
    youtube_link = models.URLField()

    def __str__(self):
        return self.name

class MovieTicket(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)  # Or link to your User model
    purchase_date = models.DateField()
    # Add more fields as needed