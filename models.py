from django.db import models
from django.contrib import admin
from django import forms

class Order(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    cart_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} - {self.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.item_name} x{self.item_quantity} for Order {self.order.id}"


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    guests = models.IntegerField()
    reservation_date = models.DateField()
    reservation_time = models.TimeField()