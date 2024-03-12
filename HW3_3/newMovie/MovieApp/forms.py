from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'director', 'release_year', 'budget', 'runtime', 'rating', 'genre', 'image_url', 'youtube_url']
