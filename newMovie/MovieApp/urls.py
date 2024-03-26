# myproject/urls.py (Assuming your Django project is named myproject)
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views
from MovieApp.views import MovieLoginView

urlpatterns = [
    path('login/', views.MovieLoginView.as_view(), name='movie_login'),
    path('', include('newMovie.urls')),  # Assuming your app is named MovieApp
]