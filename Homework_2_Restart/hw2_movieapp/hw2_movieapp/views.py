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
    
def movie_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image_url = request.POST.get('image_url')
        image_classpath = request.POST.get('image_classpath')
        youtube_link = request.POST.get('youtube_link')
        
        # Create a new movie instance and save to the database
        Movie.objects.create(
            name=name, 
            image_url=image_url, 
            image_classpath=image_classpath, 
            youtube_link=youtube_link
        )
        return redirect('movie_list')  # Redirect to the movie list page after adding
    return render(request, 'add.html')