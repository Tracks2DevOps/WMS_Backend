# import viewsets
from rest_framework import viewsets, generics

# import local data
from .serializers import OrdersSerializer
from .models import WarehouseOrders

# import filtering stuff
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Vue API
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create API view
@api_view(['GET'])
def get_orders(request):
    orders = WarehouseOrders.objects.all()
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)


# create a viewset
class OrdersViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = WarehouseOrders.objects.all()
    # specify serializer to be used
    serializer_class = OrdersSerializer
    # create filters
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('sales_order', 'status_choices', 'customer_name', )
