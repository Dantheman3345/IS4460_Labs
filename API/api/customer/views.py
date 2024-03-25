from django.shortcuts import render
from rest_framework import generics
from .models import Customer, Order
from .serializers import CustomerSerializer
from .serializers import OrderSerializer

class CustomerListCreateView(generics.ListCreateAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
# Create your views here.



class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer