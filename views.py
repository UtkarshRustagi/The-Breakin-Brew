# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import OrderSerializer
# from .models import Order

# class OrderCreateAPIView(APIView):
#     def post(self, request):
#         try:
#             serializer = OrderSerializer(data=request.data)
#             if serializer.is_valid():
#                 order=serializer.save()
#                 return Response({"order_id":order.id}, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # Create your views here.




# from decimal import Decimal
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Order, OrderItem
# from .serializers import OrderSerializer
# from collections import Counter, defaultdict

# class OrderCreateAPIView(APIView):
#     def post(self, request):
#         data = request.data
#         name = data.get('name')
#         mobile = data.get('mobile_number')
#         address = data.get('address')
#         cart_total = data.get('cart_total')
#         item_names = data.get('item_name_list', [])
#         item_prices = data.get('item_price_list', [])

#         if len(item_names) != len(item_prices):
#             return Response({'error': 'Item name and price list lengths do not match.'}, status=status.HTTP_400_BAD_REQUEST)

#         # Count quantities for each item
#         # 
#         item_map = defaultdict(int)
#         for i in range(len(item_names)):
#             key = (item_names[i], item_prices[i])
#             item_map[key] += 1

#         # Create Order
#         order = Order.objects.create(
#             name=name,
#             mobile_number=mobile,
#             address=address,
#             cart_total=cart_total
#         )

   
#         for (item_name, item_price), quantity in item_map.items():
#             OrderItem.objects.create(
#                 order=order,
#                 item_name=item_name,
#                 item_price=Decimal(item_price),
#                 item_quantity=quantity
#             )



#         return Response({'order_id': order.id}, status=status.HTTP_201_CREATED)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from decimal import Decimal

class OrderCreateAPIView(APIView):
    def post(self, request):
        data = request.data

        name = data.get('name')
        mobile_number = data.get('mobile_number')
        address = data.get('address')
        cart_total = data.get('cart_total')
        item_name_list = data.get('item_name_list', [])
        item_price_list = data.get('item_price_list', [])

        if len(item_name_list) != len(item_price_list):
            return Response({'error': 'Mismatched item name and price lists.'}, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Create order
        order = Order.objects.create(
            name=name,
            mobile_number=mobile_number,
            address=address,
            cart_total=Decimal(str(cart_total))
        )

        # ✅ Build item-count from scratch (fresh each time)
        counted_items = {}

        for idx in range(len(item_name_list)):
            item_name = item_name_list[idx].strip()
            item_price = Decimal(str(item_price_list[idx]))

            key = f"{item_name}|{item_price}"  # unique key

            if key not in counted_items:
                counted_items[key] = {
                    'name': item_name,
                    'price': item_price,
                    'quantity': 0
                }
            else:
                counted_items[key]['quantity'] += 1

        # ✅ Save each counted item to DB
        for item in counted_items.values():
            OrderItem.objects.create(
                order=order,
                item_name=item['name'],
                item_price=item['price'],
                item_quantity=item['quantity']
            )

        return Response({'order_id': order.id}, status=status.HTTP_201_CREATED)
    
from django.http import JsonResponse
from datetime import datetime, timezone
from .models import Reservation


class reservationCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        name = data.get('name')
        email = data.get('email')
        guests = data.get('guests')
       
        reservation = Reservation.objects.create(
            name=name,
            email=email,
            guests=guests,
            reservation_date=timezone.now().date(),
            reservation_time=timezone.now().time(),
        )

        return Response({'message': 'Reservation successful!'}, status=200)
        return JsonResponse({'error': 'Invalid request'}, status=400)
        # Validate the request data
