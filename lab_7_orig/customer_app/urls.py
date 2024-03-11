# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.CustomerList.as_view(), name='customer-list'),
    path('edit/<int:customer_id>/', views.CustomerEdit.as_view(), name='customer-edit'),
    path('order_list/', views.OrderList.as_view(), name='order-list'),
    path('order_edit/<int:order_id>/', views.OrderEdit.as_view(), name='order-edit'),
    path('order_edit/', views.OrderEdit.as_view(), name='order-edit'),
    path('order_delete/<int:order_id>/', views.OrderDelete.as_view(), name='order-delete'),

]


