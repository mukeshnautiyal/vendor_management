from rest_framework.serializers import (
    Serializer, ModelSerializer, PrimaryKeyRelatedField, CharField
)
from vendor.models.users import User
from rest_framework import serializers

class VendorInfo(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','contact_details','email','is_active',"address","vendor_code"]
        #depth =1

class VendorBaseSerializer(ModelSerializer):
   
    user = VendorInfo(read_only=True)
    class Meta:
        """ Meta subclass """
        model = User
        fields = '__all__'


class VendorListSerializer(VendorBaseSerializer):
    class Meta:
        model = User
        fields = ('id','name','contact_details','email','is_active',"address","vendor_code")
       
    def to_representation(self, instance):
        try:
            rep = super(VendorListSerializer, self).to_representation(instance)            
            return rep    
        except Exception as E:
            print(E)


class VendorAddSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    contact_details = serializers.CharField(required=True)
    address = serializers.CharField(required=False,allow_blank=True)

class UpdateVendorSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    contact_details = serializers.CharField(required=True)