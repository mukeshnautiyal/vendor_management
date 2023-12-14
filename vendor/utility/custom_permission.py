
from rest_framework import permissions
from vendor.models.users import User


class CustomerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = User.objects.get(username=request.user.username)
        if user.role.name == "Admin" or user.role.name == "Super Admin":
            return True
        else:
            self.message = 'Only super admin and admin can perform this action.'
            return False