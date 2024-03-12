from django import forms
from customer_app.models import Customer,Order
from .models import Movie

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
    
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'director', 'release_year', 'budget', 'runtime', 'rating', 'genre']
    

    