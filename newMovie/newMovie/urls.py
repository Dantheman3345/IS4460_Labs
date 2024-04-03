"""
URL configuration for newMovie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# MovieApp/urls.py
from django.urls import path
from MovieApp import views
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from MovieApp.views import MovieLoginView, UserListView


urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    #path('login/', LoginView.as_view(template_name='your_template_name.html'), name='login'),
    path('login/', MovieLoginView.as_view(), name='movie_login'),
    #path('login/', views.MovieLoginView.as_view(), name='movie_login'),
    path('logout/', views.MovieLogoutView.as_view(), name='movie_logout'),
    path('admin/', admin.site.urls),
    path('list/', views.MovieListView.as_view(), name='movie_list'),
    path('details/<int:pk>/', views.MovieDetailView.as_view(), name='movie_details'),
    path('add/', views.MovieCreateView.as_view(), name='movie_add'),
    path('update/<int:pk>/', views.MovieUpdateView.as_view(), name='movie_update'),
    path('delete/<int:pk>/', views.MovieDeleteView.as_view(), name='movie_delete'),
    # API URLs remain the same
    path('api/movies/', views.MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('api/movies/<int:pk>/', views.MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-retrieve-update-destroy'),
]
