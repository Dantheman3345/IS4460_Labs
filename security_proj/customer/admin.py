from django.contrib import admin

# Register your models here.

from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    pass # Empty admin class for now
admin.site.register(Customer)
