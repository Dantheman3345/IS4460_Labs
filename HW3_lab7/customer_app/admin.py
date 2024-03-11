from django.contrib import admin

# Register your models here.


from customer_app.models import Customer,Movie
from .models import Movie




class CustomerAdmin(admin.ModelAdmin):
    pass


#admin.site.register(Customer)
admin.site.register(Movie)