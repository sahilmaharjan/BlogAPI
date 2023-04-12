from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


# Customize error message
class UpdateBlogDenied(PermissionDenied):
    default_detail = 'Error: You do not have permission to edit this blog.'

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_authenticated:
            print(view,"valid authenticated")
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj == request.user.id:
            print(obj,"valid object authenticated")
            return True
        raise UpdateBlogDenied()
    
class IsOwner(permissions.BasePermission):
    """
    Custom permission to allow only the owner of a blog to delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the requesting user is the owner of the blog
        print("obj authro =====>", obj.id)
        print("req user====>", request.user.id)
        return obj.id == request.user.id