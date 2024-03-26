
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from .serializers import MovieSerializer
from rest_framework import generics
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Movie
from .forms import MovieForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView
from .forms import CustomLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView


# MovieLoginView for handling login
class MovieLoginView(LoginView):
    form_class = AuthenticationForm  # Utilizes Django's built-in authentication form
    template_name = 'movie_login.html'  # Specifies the template used for the login page
    #redirect_authenticated_user = True  # Redirects users who are already authenticated

    def get_success_url(self):
        # This method returns the URL to redirect to after a successful login
        return reverse_lazy('movie_list')  # Redirects to the 'movie_list' URL

# MovieLogoutView for handling logout
class MovieLogoutView(LogoutView):
    next_page = reverse_lazy('movie_login')  # Redirects to the login page after logout





from django.views.generic import ListView

#class MovieListView(LoginRequiredMixin, ListView):
    # Your existing ListView code here
#    login_url = '/login/'  # Redirect to login page if not authenticated



class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieListView(TemplateView, LoginRequiredMixin):
    template_name = 'movie_list.html'
    login_url = '/login/'  # Redirect to login page if not authenticated
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        return context

class MovieDetailView(LoginRequiredMixin, DetailView):
    model = Movie
    template_name = 'movie_details.html'
    context_object_name = 'movie'
    login_url = '/login/'  # Redirect to login page if not authenticated

class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')
    login_url = '/login/'  # Redirect to login page if not authenticated

class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')
    login_url = '/login/'  # Redirect to login page if not authenticated

class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'movie_delete.html'
    success_url = reverse_lazy('movie_list')
    login_url = '/login/'  # Redirect to login page if not authenticated