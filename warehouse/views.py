# import viewsets
from rest_framework import viewsets, generics

# import local data
from .serializers import OrdersSerializer
from .models import WarehouseOrders

# import filtering stuff
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


# create a viewset
class OrdersViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = WarehouseOrders.objects.all()
    # specify serializer to be used
    serializer_class = OrdersSerializer
    # create filters
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('sales_order', 'status_choices', 'customer_name', )
