from rest_framework.serializers import (
    Serializer, ModelSerializer, PrimaryKeyRelatedField, CharField
)
from vendor.models.orders import Order_Purchase
from vendor.models.users import User
from rest_framework import serializers

class PurchaseOrderInfo(ModelSerializer):
    class Meta:
        model = Order_Purchase
        fields = ['id','po_number','order_date','delivery_date','items',"qauntity","status","quality_rating","acknowledgment_date","issue_date"]
        #depth =1

class PurchaseOrderBaseSerializer(ModelSerializer):
   
    user = PurchaseOrderInfo(read_only=True)
    class Meta:
        """ Meta subclass """
        model = Order_Purchase
        fields = '__all__'


class PurchaseOrderListSerializer(PurchaseOrderBaseSerializer):
    class Meta:
        model = Order_Purchase
        fields = ('id','po_number','order_date','delivery_date','items',"qauntity","status","quality_rating","acknowledgment_date","issue_date")
       
    def to_representation(self, instance):
        try:
            rep = super(PurchaseOrderListSerializer, self).to_representation(instance)
            vendor = User.objects.get(pk=instance.vendor.id)
            rep["vendor"] = {"id":vendor.id,"vendor_code":vendor.vendor_code}
            return rep    
        except Exception as E:
            print(E)


class AddPurchaseOrderSerializer(serializers.Serializer):
    vendor_code = serializers.CharField(required=True)
    items = serializers.JSONField(required=True)
    quantity = serializers.CharField(required=True)

class UpdatePurchaseOrdersSerializer(serializers.Serializer):
    items = serializers.CharField(required=False)
    quantity = serializers.CharField(required=False)
    flag = serializers.CharField(required=True)