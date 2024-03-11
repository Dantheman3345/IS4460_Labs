from django.contrib import admin

# Register your models here.


from customer_app.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer)