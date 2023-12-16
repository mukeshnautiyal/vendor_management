from rest_framework import generics
from rest_framework.response import Response
from vendor.custom_serializers.user_serializers import VendorListSerializer,VendorAddSerializer,UpdateVendorSerializer
from vendor.models.users import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from vendor.utility.errorhandler import Custom_Queryset_Response
from vendor.utility.custompagination import CustomPageNumberPagination
from ..utility.decorators import IsAdmin
from vendor.utility.common_function import GenerateCode

class CreateVendor(generics.CreateAPIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    permission_classes = (IsAuthenticated,IsAdmin)
    serializer_class = VendorAddSerializer
    
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            response = {'status':200 , "message":"Vendor Successfully Added","data":None}
            serializer = self.serializer_class(data=data)
            if not  serializer.is_valid():
                data = {"status":400,"message":"Invalid Data","data":{"message":"Invalid Data",'form_errors':serializer.errors}}
                return Response(data)
            if User.objects.filter(email=data["email"]).exists():
                data = {"status":401,"message":"User Already exist with this email id","data":None}
                return Response(data)
            user = User.objects.create(email=data["email"],username=data["email"],is_active=1,name=data["name"],address=data["address"],contact_details=data["contact_details"],role_id=3)
            user.set_password(data['password'])
            user.save()
            User.objects.filter(pk=user.id).update(vendor_code=GenerateCode(user.id))
            return Response(response)
        except Exception as e:
            response = {'status':500 , "message":"Something went wrong","data":None,"trace":str(e)}
            return Response(response)


class VendorListView(generics.ListAPIView):
    pagination_class = CustomPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    permission_classes = (IsAuthenticated,IsAdmin)
    serializer_class = VendorListSerializer
    
    def get_queryset(self):
        queryset = User.objects.filter(is_active=True).filter(role__name="Vendor").order_by("-id")
        return queryset

    def get(self, request, *args, **kwargs):
        try:
            data= Custom_Queryset_Response (self,request,VendorListSerializer)
            return Response(data)
        except Exception as E:
            data = {"status":500,"message":"Something went wrong!","data":{"trace":str(E)}}
            return Response(data)


class DetailView(generics.RetrieveAPIView):
    pagination_class = CustomPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    permission_classes = (IsAuthenticated,IsAdmin)
    serializer_class = VendorListSerializer
    
    def get_queryset(self):
        pk=self.kwargs['pk']
        queryset = User.objects.filter(is_active=True,id=pk,role__name="Vendor")
        return queryset

    def get(self, request, *args, **kwargs):
        try:
            data= Custom_Queryset_Response (self,request,self.serializer_class)
            return Response(data)
        except Exception as E:
            data = {"status":500,"message":"Something went wrong!","data":{"trace":str(E)}}
            return Response(data)


class UpdateView(generics.UpdateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    permission_classes = (IsAuthenticated,IsAdmin)
    serializer_class = UpdateVendorSerializer
    
    def put(self,request,pk):
        try:
            response = {'status':200 , "message":"Vendor Updated Successfully","data":None}
            instance = User.objects.get(pk=pk)
            serializer = self.serializer_class(instance, data=request.data)
            if not  serializer.is_valid():
                data = {"status":400,"message":"Invalid Data","data":{"message":"Invalid Data",'form_errors':serializer.errors}}
                return Response(data)
            elif serializer.is_valid():
                serializer.save()
            return Response(response)
        except Exception as e:
            response = {'status':500 , "message":"Something went wrong","data":None,"trace":str(e)}
            return Response(response)


class DeleteView(generics.DestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def delete(self, request,pk):
        try:
            user_details = User.objects.get(id=pk)
            User.objects.filter(id=pk).update(is_active=False,username=user_details.username+"_"+str(pk),email=user_details.email+"_"+str(pk))
            return Response({'status':200 , "message":"User Removed Successfully","data":None})
        except Exception as E:
            data = {"status":500,"message":"Something went wrong!","data":{"trace":str(E)}}
            return Response(data)