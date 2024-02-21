from django.shortcuts import render
from .models import Movie, MovieTicket
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'list.html', {'movies': movies})



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

# Define additional views for add, details, update, ticket purchase, delete, etc.
    
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from .models import Movie  # Make sure this import is correct
import re

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