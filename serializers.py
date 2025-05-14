from rest_framework import serializers
from .models import Order, OrderItem, Reservation

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['item_name', 'item_price', 'item_quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'name', 'mobile_number', 'address', 'cart_total', 'items']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'guests', 'date', 'time']