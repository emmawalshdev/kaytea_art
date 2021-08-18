from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    # make line item total readonly
    readonly_fields = ('lineitem_total',)


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)
    fields = ('order_number', 'date', 'first_name', 'last_name', 'email',
              'mobile_number', 'address_line1', 'address_line2',
              'town_or_city', 'county', 'country', 'postcode',
              'order_total', 'delivery_cost', 'grand_total',)

    list_display = ('order_number', 'date', 'first_name', 'last_name', 'email',
                    'mobile_number', 'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)

# register the order model and orderadmin
admin.site.register(Order, OrderAdmin)
