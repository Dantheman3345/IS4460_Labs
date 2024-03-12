
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def movie_login(request):
    return render(request, 'movie_login.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_details(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movie_details.html', {'movie': movie})

def movie_add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie_form.html', {'form': form})

def movie_update(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie_form.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie

def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movie_delete.html', {'movie': movie})