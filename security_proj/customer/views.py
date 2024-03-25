from django.shortcuts import render
from django.views import View
from .models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin
#chatgpt will try to use function based views, use class based views please.
# Create your views here.

class CustomerListView(LoginRequiredMixin,View):

    def get(self,request):
        customers = Customer.objects.all()
        return render(request=request,
                      template_name='customer/customer_list.html',
                      context = {'customers':customers}
                      )
