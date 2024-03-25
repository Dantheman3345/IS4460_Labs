from django.urls import path
from .views import CustomerListView

urlpatterns = [
    path('list/',CustomerListView.as_view(),name='customer-list'),
    
]