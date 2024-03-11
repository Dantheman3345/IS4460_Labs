# customer_app -> urls.py
from django.urls import path
from . import views
from .views import MovieListView, MovieUpdateView, MovieDeleteView, MovieCreateView, OrderEdit

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/edit/<int:pk>/', MovieUpdateView.as_view(), name='movie-edit'),
    path('movies/delete/<int:pk>/', MovieDeleteView.as_view(), name='movie-delete'),
    path('movies/add/', MovieCreateView.as_view(), name='movie-add'),
    path('customer/movies/edit/<int:pk>/', MovieUpdateView.as_view(), name='movie-update'),
    path('customer/orders/edit/<int:order_id>/', OrderEdit.as_view(), name='order-update'),

    path('list/', views.CustomerList.as_view(), name='customer-list'),
    path('edit/<int:customer_id>/', views.CustomerEdit.as_view(), name='customer-edit'),
    path('order_list/', views.OrderList.as_view(), name='order-list'),
    path('order_edit/<int:order_id>/', views.OrderEdit.as_view(), name='order-edit'),
    path('order_edit/', views.OrderEdit.as_view(), name='order-edit'),
    path('order_delete/<int:order_id>/', views.OrderDelete.as_view(), name='order-delete'),

]

