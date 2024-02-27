my_new_customer = Customer()

my_new_customer.name ="ABC Corp."

my_new_customer.save()

xyz_corp = Customer()
xyz_corp.name = "XYZ Corporation"
xyz_corp.save()
from customer.models import Customer
Customer.objects.get(pk=1)
from customer.models import Customer
Customer.objects.get(pk=1)
customer_one = Customer.objects.get(pk=1)
customer_one.name
customer_one.name = "Some new Name"
customer_one.save()
customer_one.delete()
Customer.objects.create(name="Plumbing Specialists")
Customer.objects.create(name="Electronics Experts")
Customer.objects.create(name="Structural Consultants")
customer = Customer.objects.get(name='Electronics Experts')
customer.name
results = Customer.objects.filter(name_startswith=("Plumb"))
customers
customers = Customer.objects.all()
the_customer = Customer.objects.get(pk=4)
from customer.models import Customer
the_customer = Customer.objects.get(pk=4)
from customer.models import Customer,Order
order1 = Order(customer=the_customer,total_price=24.99,total_items=3)
order1.save()
order2 = Order(customer=the_customer,total_price=12.99,total_items=1)
order2.save()