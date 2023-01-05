import dateutil.utils
from django.db import models
import datetime
from django.utils import timezone

today = timezone.now().date()


class WarehouseOrders(models.Model):
    sales_order = models.IntegerField("Sales Order Number")
    # Create choices for status
    SHIPPED = 'Shipped from warehouse'
    RECEIVED = 'Received at warehouse'
    PENDING = 'Not received'
    SHIPPING_STATUS_CHOICES = [
        (SHIPPED, 'Shipped'),
        (RECEIVED, 'Received'),
        (PENDING, 'Pending'),
    ]
    status_choices = models.TextField(
        "Status",
        choices=SHIPPING_STATUS_CHOICES,
        default=PENDING,
    )

    customer_name = models.TextField("Customer Name")
    equipment_cost = models.IntegerField("Cost of Equipment")
    final_destination = models.TextField("Final Destination")
    internal_contacts = models.TextField("Internal Contacts")
    product_description = models.TextField("Short Description of Order")
    inbound_carrier = models.TextField("Incoming Carrier Name")
    inbound_tracking = models.TextField("Incoming Tracking Number")
    date_received = models.DateField("Date Received by Warehouse", default=dateutil.utils.today())
    num_pallets = models.IntegerField("Number of Pallets Received")
    num_boxes = models.IntegerField("Number of boxes Received")
    length = models.IntegerField("Length (in inches)")
    width = models.IntegerField("Width (in inches)")
    height = models.IntegerField("Height (in inches)")
    weight = models.IntegerField("Weight (in pounds)")
    # Add choices for lithium stickers
    lithium = models.TextField("Lithium Battery Sticker Present")
    serial_num = models.TextField("Serial Numbers")
    country_origin = models.TextField("Country of Origin")
    outbound_carrier = models.TextField("Outgoing Carrier Name")
    outbound_tracking = models.TextField("Outgoing Tracking Number")
    out_pallets = models.IntegerField("Number of Pallets Shipped")
    out_boxes = models.IntegerField("Number of Boxes Shipped")
    date_shipped = models.DateField("Date Shipped From Warehouse", default=timezone.now)
    # attachments = models.FileField("Attachments (ie. Bill of Ladings, Packing List, etc.)")

    def __str__(self):
        return self.customer_name
