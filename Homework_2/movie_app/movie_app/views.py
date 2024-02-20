from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Movie  # Import your Movie model
from django.contrib.auth.views import LoginView

# View for displaying the list of movies
class MovieListView(ListView):
    model = Movie
    template_name = 'templates/movie_list.html'
    context_object_name = 'movies'

# View for displaying details of a single movie
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'

# View for adding a new movie
class MovieCreateView(CreateView):
    model = Movie
    template_name = 'movies/movie_form.html'
    fields = ['name', 'image', 'youtube_link']  # Specify the fields you want to include in the form

    def get_success_url(self):
        return reverse_lazy('movie-list')  # Redirect to movie list view after successful creation

# View for updating a movie
class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'movies/movie_form.html'
    fields = ['name', 'image', 'youtube_link']  # Specify the fields you want to include in the form

    def get_success_url(self):
        return reverse_lazy('movie-list')  # Redirect to movie list view after successful update

# View for deleting a movie
class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    context_object_name = 'movie'

    def get_success_url(self):
        return reverse_lazy('movie-list')  # Redirect to movie list view after successful deletion

class MovieLoginView(LoginView):
    template_name = 'movies/movie_login.html'
    redirect_authenticated_user = True  # Redirect users to another page if they are already logged in

    def get_success_url(self):
        return reverse_lazy('movie-list')  # Redirect to the movie list page after a successful login    
    

def movie_add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie-list')  # Redirect to the movie list view after saving
    else:
        form = MovieForm()
    return render(request, 'movie_app/movie_add.html', {'form': form})