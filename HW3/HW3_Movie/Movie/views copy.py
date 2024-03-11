from django.shortcuts import render
from .models import Movie, MovieTicket
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from .models import Movie  # Make sure this import is correct
import re


def movie_list(request):
    movies = Movie.objects.all()  # This retrieves all movie instances
    return render(request, 'list.html', {'movies': movies})

def home_view(request):
    # Check if user is authenticated and redirect to movie list if true
    if request.user.is_authenticated:
        return redirect('movie_list')
    # Render login.html template as the default page if user is not authenticated
    return render(request, 'login.html')

def movie_details(request, movie_id):
    # Fetch the movie by movie_id
    #movie = get_object_or_404(Movie, movie_id=movie_id)
    #return render(request, 'details.html', {'movie': movie})
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie_details.html', {'movie': movie})


def movie_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('movie_list')  # Adjust the redirect as needed
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid login'})
    else:
        return render(request, 'login.html')

def update_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_id)
        movie.title = request.POST['title']
        movie.description = request.POST['description']
        # Add any other fields you need to update
        movie.save()

        # Use the reverse function to generate the URL for the movie_details view
        # and redirect the user to that page
        return HttpResponseRedirect(reverse('movie_details', args=(movie.id,)))
    


def movie_add(request):
    if request.method == 'POST':
        # Existing fields capture
        title = request.POST.get('title')
        description = request.POST.get('description')
        director = request.POST.get('director')
        release_year = request.POST.get('release_year')
        budget_input = request.POST.get('budget')
        runtime = request.POST.get('runtime')
        rating = request.POST.get('rating')
        genre = request.POST.get('genre')
        
        # New fields capture
        name = request.POST.get('name')
        image_url = request.POST.get('image_url')
        image_classpath = request.POST.get('image_classpath')
        youtube_link = request.POST.get('youtube_link')

        # Convert budget input to a decimal
        try:
            # Remove commas and other non-numeric characters except for "million" or "m"
            budget_cleaned = re.sub(r'[^\d.]+', '', budget_input.lower())
            if 'million' in budget_input.lower() or 'm' in budget_input.lower():
                budget = float(budget_cleaned) * 1000000
            else:
                budget = float(budget_cleaned)
        except ValueError:
            return render(request, 'add.html', {
                'error': 'Invalid budget format. Please enter a numeric value.'
            })

        # Create a new movie instance including the new fields and save to the database
        Movie.objects.create(
            title=title,
            description=description,
            director=director,
            release_year=release_year,
            budget=budget,  # Use the converted budget
            runtime=runtime,
            rating=rating,
            genre=genre,
            name=name,  # New field
            image_url=image_url,  # New field
            image_classpath=image_classpath,  # New field
            youtube_link=youtube_link  # New field
        )
        return redirect('movie_list')
    return render(request, 'add.html')

def delete_all_movies(request):
    Movie.objects.all().delete()
    return redirect('movie_list')  # Redirect to the movie list view after deletion

def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.delete()
    return redirect('movie_list')  # Redirect to the movie list view after deletion

