from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from .models import Customer, Order, Movie
from .forms import CustomerForm, OrderForm
from django.views.generic import ListView, UpdateView, DeleteView, TemplateView, CreateView
# Create your views here.


class LoginView(TemplateView):
    template_name = 'customer_app/login.html'

# Movie List View
class MovieListView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movie_list.html'

# Movie Edit View
class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['title', 'description', 'director', 'release_year', 'budget', 'runtime', 'rating', 'genre']
    template_name = 'customer_app/order_edit.html'
    success_url = reverse_lazy('movie-list')

# Movie Delete View
class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'customer_app/order_delete.html'
    success_url = reverse_lazy('movie-list')

class MovieCreateView(CreateView):
    model = Movie
    fields = ['title', 'description', 'director', 'release_year', 'budget', 'runtime', 'rating', 'genre']
    template_name = 'movie_form.html'  # Use the appropriate template
    success_url = reverse_lazy('movie-list')  # Redirect to the movie list after creation








class CustomerList(View):

    def get(self,request):

        customers = Customer.objects.all()

        return render(request = request,template_name = 'customer_app/customer_list.html',context = {'customers':customers})
    
class CustomerEdit(View):

    def get(self,request,customer_id):

        customer = Customer.objects.get(pk=customer_id)
        form = CustomerForm(instance=customer)

        return render(request = request,template_name = 'customer_app/customer_edit.html',context = {'customer':customer,'form':form})
    
    def post(self,request,customer_id):

        customer = Customer.objects.get(pk=customer_id)
        form = CustomerForm(request.POST,instance=customer)

        if form.is_valid():
            customer = form.save()
        
        return render(request = request,template_name = 'customer_app/customer_edit.html',context = {'customer':customer,'form':form})
    


class OrderList(View):

    def get(self,request):

        orders = Order.objects.all()
        movies = Movie.objects.all()

        return render(request = request,template_name = 'customer_app/order_list.html',context = {'orders':orders,'movies':movies})
    
class OrderEdit(View):

    def get(self,request,order_id=None):

        if order_id:
            order = Order.objects.get(pk=order_id)
        else:
            order = Order()

        form = OrderForm(instance=order)

        return render(request = request,
                      template_name = 'customer_app/order_edit.html',
                      context = {'order':order,'form':form})
    
    def post(self,request,order_id=None):

        if order_id:
            order = Order.objects.get(pk=order_id)
        else:
            order = Order()

        form = OrderForm(request.POST,instance=order)

        if form.is_valid():
            order = form.save()

            return redirect(reverse("order-list"))
        
        return render(request = request,template_name = 'customer_app/order_edit.html',context = {'order':order,'form':form})
    




class OrderDelete(View):

    def get(self,request,order_id=None):

        if order_id:
            order = Order.objects.get(pk=order_id)
        else:
            order = Order()

      


        form = OrderForm(instance=order)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'customer_app/order_delete.html',context = {'order':order,'form':form})
      
    
    def post(self,request,order_id=None):

        order = Order.objects.get(pk=order_id)

        form = OrderForm(request.POST,instance=order)

        order.delete()

        return redirect(reverse("order-list"))
    