from django.contrib.auth.models import User, Group
# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import WarehouseOrders


# Create a model serializer
class OrdersSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = WarehouseOrders
        fields = (
            'sales_order',
            'status_choices',
            'customer_name',
            'equipment_cost',
            'final_destination',
            'internal_contacts',
            'product_description',
            'inbound_carrier',
            'inbound_tracking',
            'date_received',
            'num_pallets',
            'num_boxes',
            'length',
            'width',
            'height',
            'weight',
            'lithium',
            'serial_num',
            'country_origin',
            'outbound_carrier',
            'outbound_tracking',
            'out_pallets',
            'out_boxes',
            'date_shipped',
            # attachments = models.FileField()
        )


"""class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']"""