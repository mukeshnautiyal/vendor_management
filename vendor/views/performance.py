from rest_framework import generics
from rest_framework.response import Response
from vendor.models.orders import Order_Purchase
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from ..utility.decorators import IsAdmin
from django.db.models import Avg


class VendorPerformance(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    permission_classes = (IsAuthenticated,IsAdmin)

    def get(self, request, *args, **kwargs):
        try:
            pk=self.kwargs['pk']
            queryset = Order_Purchase.objects.filter(vendor_id=pk)
            on_time = queryset.values("vendor_id__on_time_delivery_rate","vendor_id__average_response_time")
            on_time_delivery_rate=on_time[0]["vendor_id__on_time_delivery_rate"]
            ord_rate = queryset.aggregate(Avg('quality_rating'))
            quality_rating = ord_rate["quality_rating__avg"]
            response_time = on_time[0]["vendor_id__average_response_time"]
            op = queryset.filter(issue_date__isnull=True).count()
            try:
                fulfilment_rate = round((op*100)/queryset.count(),2)
            except:
                pass
            data = {"on_time_delivery_rate":on_time_delivery_rate,"quality_rating":quality_rating,"response_time":response_time,"fulfilment_rate":fulfilment_rate}
            return Response({"status":200,"message":"success","data":data})
        except Exception as E:
            data = {"status":500,"message":"Something went wrong!","data":{"trace":str(E)}}
            return Response(data)