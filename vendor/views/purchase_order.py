from rest_framework import generics
from rest_framework.response import Response
from vendor.models.users import User
from vendor.models.orders import Order_Purchase
from vendor.custom_serializers.purchase_order_serializers import AddPurchaseOrderSerializer, PurchaseOrderListSerializer,UpdatePurchaseOrdersSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from vendor.utility.errorhandler import Custom_Queryset_Response
from vendor.utility.custompagination import CustomPageNumberPagination
from ..utility.decorators import IsAdmin
from vendor.utility.common_function import GetOrderNumber
from datetime import datetime

class CreatePurchaseOrders(generics.CreateAPIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    permission_classes = (IsAuthenticated,IsAdmin)
    serializer_class = AddPurchaseOrderSerializer
    
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            response = {'status':200 , "message":"Purchase Order Successfully Added","data":None}
            serializer = self.serializer_class(data=data)
            if not  serializer.is_valid():
                data = {"status":400,"message":"Invalid Data","data":{"message":"Invalid Data",'form_errors':serializer.errors}}
                return Response(data)
            vendor = User.objects.get(vendor_code=data["vendor_code"],role__name="Vendor")
            od = Order_Purchase.objects.create(vendor=vendor,items=data["items"],qauntity=data["quantity"],status="Pending")
            Order_Purchase.objects.filter(pk=od.id).update(po_number=GetOrderNumber(od.id))
            return Response(response)
        except Exception as e:
            response = {'status':500 , "message":"Something went wrong","data":None,"trace":str(e)}
            return response


class PurposeOrdersListView(generics.ListAPIView):
    pagination_class = CustomPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = PurchaseOrderListSerializer
    
    def get_queryset(self):
        vendor = self.request.GET.get('vendor_code')
        queryset = Order_Purchase.objects.filter()
        if vendor != "" and vendor != None:
            queryset = queryset.filter(vendor__vendor_code=vendor).order_by("-id")
        else:
            queryset = queryset.order_by("-id")
        return queryset

    def get(self, request, *args, **kwargs):
        try:
            data= Custom_Queryset_Response (self,request,PurchaseOrderListSerializer)
            return Response(data)
        except Exception as E:
            data = {"status":500,"message":"Something went wrong!","data":{"trace":str(E)}}
            return Response(data)




class PurchaseDetailsDetailView(generics.RetrieveAPIView):
    pagination_class = CustomPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    permission_classes = (IsAuthenticated,IsAdmin)
    serializer_class = PurchaseOrderListSerializer
    
    def get_queryset(self):
        pk=self.kwargs['pk']
        queryset = Order_Purchase.objects.filter(id=pk)
        return queryset

    def get(self, request, *args, **kwargs):
        try:
            data= Custom_Queryset_Response (self,request,self.serializer_class)
            return Response(data)
        except Exception as E:
            data = {"status":500,"message":"Something went wrong!","data":{"trace":str(E)}}
            return Response(data)




class UpdatePurchaseOrderView(generics.UpdateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    permission_classes = (IsAuthenticated,IsAdmin)
    serializer_class = UpdatePurchaseOrdersSerializer
    
    def put(self,request,pk):
        try:
            data = request.data
            response = {'status':200 , "message":"Purchase Order Updated Successfully","data":None}
            serializer = self.serializer_class(data=data)
            if not  serializer.is_valid():
                data = {"status":400,"message":"Invalid Data","data":{"message":"Invalid Data",'form_errors':serializer.errors}}
                return Response(data)
            if data["flag"] == "status":
                Order_Purchase.objects.filter(pk=pk).update(status="Completed")
            elif data["flag"] == "acknowledgment_date":
                Order_Purchase.objects.filter(pk=pk).update(acknowledgment_date=datetime.now())
            else:
                Order_Purchase.objects.filter(pk=pk).update(items=data["items"],quantity=data["quantity"])
            return Response(response)
        except Exception as e:
            response = {'status':500 , "message":"Something went wrong","data":None,"trace":str(e)}





class DeletePurchaseOrder(generics.DestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    permission_classes = (IsAuthenticated,IsAdmin)
    
    def delete(self, request,pk):
        try:
            Order_Purchase.objects.filter(id=pk).update(is_deleted=True)
            return Response({'status':200 , "message":"Purchase Order Removed Successfully","data":None})
        except Exception as E:
            data = {"status":500,"message":"Something went wrong!","data":{"trace":str(E)}}
            return Response(data)








