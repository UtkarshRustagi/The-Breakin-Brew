from django.contrib import admin
from .models import Order, OrderItem, Reservation

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'item_name', 'item_quantity', 'item_price')
    search_fields = ('item_name',)
    list_filter = ('order__id',)

    def order_id(self, obj):
        return obj.order.id
    order_id.short_description = 'Order ID'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile_number', 'cart_total', 'address')
    search_fields = ('name', 'mobile_number')

admin.site.register(Order, OrderAdmin)

admin.site.register(OrderItem, OrderItemAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'guests', 'reservation_date', 'reservation_time')
    search_fields = ('name', 'email')
    list_filter = ('reservation_date',)
    def date(self, obj):
        return obj.reservation_datetime.date()
admin.site.register(Reservation, ReservationAdmin)
 