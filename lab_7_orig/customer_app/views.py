from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .models import Customer, Order
from .forms import CustomerForm, OrderForm
# Create your views here.

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

        return render(request = request,template_name = 'customer_app/order_list.html',context = {'orders':orders})
    
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
    