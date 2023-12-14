from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from vendor.models.users import User



class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = authenticate(username=request.data['username'], password=request.data['password'])
            if user is not None:
                refresh = RefreshToken.for_user(user)
                res = {"id":user.id,"username": user.username,"email": user.email,"refresh": str(refresh),"access": str(refresh.access_token)}
                return Response({"data":res,"status":200,"message":"User logged in successfully"})
            else:
                return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as E:
            data = {"status":500,"message":"Something went wrong!","data":{"trace":str(E)}}
            return Response(data)