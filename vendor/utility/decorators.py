from rest_framework.permissions import BasePermission
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token
import functools
from django.shortcuts import redirect
from django.contrib import messages
from vendor.models.users import User

SAFE_METHODS=['POST','GET','PUT',"PATCH","DELETE"]



class IsAdmin(BasePermission):
    message = 'Only Admin can perform this action.'

    def has_permission(self,request,view):
        try:
            if request.method in SAFE_METHODS:
                if User.objects.filter(id=request.user.id):
                    user_obj = User.objects.get(id=request.user.id)
                    if not user_obj.role.name == "Admin":
                        self.message = 'Only Admin can perform this action.'
                        return False
                    else:
                        return True
                else:
                    return None
        except Exception as error:
            self.message=str(error)
            return None

 



def AdminAuthenticationRequired(view_func, redirect_url="login"):

    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if User.objects.filter(id=request.user.id):
            user_obj = User.objects.get(id=request.user.id)
            if user_obj.role.name != "Admin" or user_obj.role.name != "Super Admin":
                return view_func(request,*args, **kwargs)
            messages.info(request, "You need to be logged out")
            return redirect(redirect_url)
    return wrapper

def verification_required(view_func, verification_url="login"):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user:
            if request.user.is_active == False:
                return view_func(request,*args, **kwargs)
            messages.info(request, "User is not active")
            return redirect(verification_url)
    return wrapper