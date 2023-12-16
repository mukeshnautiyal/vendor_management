from django.db import models
from .users import User

Status_Choice = (
    ("Pending","Pending"),
    ("Completed","Completed"),
    ("Canceled","Canceled"),
)


class Order_Purchase(models.Model):

    class Meta:
       db_table  = "order_purchase"

    id         =     models.BigAutoField(primary_key=True)
    vendor = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="vendor_id",related_query_name="vendor_user_id")
    po_number        = models.CharField(max_length=20, unique=True,blank=True)
    order_date      = models.DateTimeField(auto_now_add=True, null=True)
    delivery_date           = models.DateTimeField(default=None,null=True,blank=True)
    items = models.JSONField(null=True, default=None)
    quantity =models.IntegerField(null=True, default=None)
    status = models.CharField(max_length=30,choices = Status_Choice, default = '1')
    quality_rating = models.FloatField(null=True, default=None)
    acknowledgment_date = models.DateTimeField(default=None,null=True,blank=True)
    issue_date      = models.DateTimeField(default=None,null=True,blank=True)
    is_deleted        = models.BooleanField(default=False)

    def __str__(self):
        return self.po_number


class Historical_Performance(models.Model):

    class Meta:
       db_table  = "historical_performance"

    id         =     models.BigAutoField(primary_key=True)
    vendor = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="history_vendor_id",related_query_name="history_vendor_user_id")
    date      = models.DateTimeField(auto_now_add=True, null=True)
    ontime_delivery_date           = models.DateTimeField(auto_now=True,blank=True, null=True)
    quality_rating_avg = models.FloatField(null=True, default=None)
    average_response_time = models.FloatField(null=True,default=None )
    fulfillment_rate      = models.FloatField(null=True,default=None )

