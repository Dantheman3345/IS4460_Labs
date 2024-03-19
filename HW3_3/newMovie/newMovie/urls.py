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
from django.urls import path
from MovieApp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.movie_login, name='movie_login'),
    path('login/', views.movie_login, name='movie_login'),
    path('list/', views.movie_list, name='movie_list'),
    path('details/<int:movie_id>/', views.movie_details, name='movie_details'),
    path('add/', views.movie_add, name='movie_add'),
    path('update/<int:movie_id>/', views.movie_update, name='movie_update'),
    path('delete/<int:movie_id>/', views.movie_delete, name='movie_delete'),
    # API URLs
    path('api/movies/', views.MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('api/movies/<int:pk>/', views.MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-retrieve-update-destroy'),
]
