from django import forms
from customer_app.models import Customer,Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
    

    

    