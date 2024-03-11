"""
URL configuration for hw2_movieapp project.

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
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.movie_login, name='movie_login'),
    path('list/', views.movie_list, name='movie_list'),
    path('add/', views.movie_add, name='movie_add'),
    path('movie/details/<int:movie_id>/', views.movie_details, name='movie_details'),
    path('movie/update/<int:movie_id>/', views.update_movie, name='update_movie'),
    #path('ticket/', views.movie_ticket, name='movie_ticket'),
    #path('delete/<int:id>/', views.movie_delete, name='movie_delete'),
]
