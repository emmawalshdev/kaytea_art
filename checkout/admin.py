from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)
    fields = ('order_number', 'date', 'first_name', 'last_name', 'email',
              'address_line1', 'address_line2', 'town_or_city', 'county',
              'country', 'postcode', 'delivery_cost', 'order_total', 
              'grand_total',)