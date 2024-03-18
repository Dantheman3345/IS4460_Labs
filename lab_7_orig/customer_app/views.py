from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .models import Customer, Order, Contact
from .forms import CustomerForm, OrderForm, ContactForm
# Create your views here.

class ContactEdit(View):

    def get(self,request,contact_id=None):

        if contact_id:
            contact = Contact.objects.get(pk=contact_id)
        else:
            contact = Contact()

        form = ContactForm(instance=contact)

        return render(request = request,
                      template_name = 'customer_app/contact_edit.html',
                      context = {'contact':contact,'form':form})

    def post(self,request,contact_id=None):

        if contact_id:
            contact = Contact.objects.get(pk=contact_id)
        else:
            contact = Contact()

        form = ContactForm(request.POST,instance=contact)

        if form.is_valid():
            contact = form.save()

            return redirect(reverse("contact-edit"))
        
        return render(request = request,template_name = 'customer_app/contact_edit.html',context = {'contact':contact,'form':form})
    



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
            logo = request.FILES['logo']
            instance = customer.logo = logo
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
    