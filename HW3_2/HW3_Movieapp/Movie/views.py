from django.shortcuts import render
from .models import Movie

def login_view(request):
    return render(request, 'Movie/login.html')


def list_view(request):
    # Logic to pass context data to the template can be added here
    
    return render(request, 'Movie/list.html')



#def movie_list(request):
#    movies = Movie.objects.all()
#    return render(request, 'Movie/movie_list.html', {'movies': movies})
