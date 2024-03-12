from django.urls import path
from . import views
from .views import MovieListView, MovieUpdateView, MovieDeleteView, MovieCreateView, OrderEdit
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Movie-related URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('customer/movies/', views.MovieListView.as_view(), name='movie-list'),
    path('customer/movies/add/', views.MovieCreateView.as_view(), name='movie-add'),
    path('customer/movies/edit/<int:pk>/', views.MovieUpdateView.as_view(), name='movie-update'),
    path('customer/movies/delete/<int:pk>/', views.MovieDeleteView.as_view(), name='movie-delete'),


    # Other customer-related URLs
    path('customer/list/', views.CustomerList.as_view(), name='customer-list'),
    path('customer/edit/<int:customer_id>/', views.CustomerEdit.as_view(), name='customer-edit'),
    path('customer/order_list/', views.OrderList.as_view(), name='order-list'),
    path('customer/order_edit/<int:order_id>/', views.OrderEdit.as_view(), name='order-update'),  # Note the change here to align with your described path
    path('customer/order_delete/<int:order_id>/', views.OrderDelete.as_view(), name='order-delete'),
]

