from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)  # Movie name
    image = models.ImageField(upload_to='movies/images/')  # Path to the movie image
    youtube_link = models.URLField()  # Embed link for the YouTube trailer

    def __str__(self):
        return self.name