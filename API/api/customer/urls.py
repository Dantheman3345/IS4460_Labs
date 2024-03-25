
from .views import CustomerListCreateView, CustomerDetailView, OrderListCreateView, OrderDetailView
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(),name ='customer-detail'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
