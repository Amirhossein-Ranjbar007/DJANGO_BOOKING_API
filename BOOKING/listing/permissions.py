from rest_framework.permissions import BasePermission

class IsSpaceOwner(BasePermission):

    def has_object_permission(self, request, view, obj):

        return obj.host.user == request.user.id

class IsHost(BasePermission):

    def has_permission(self, request, view):
        message = "Only hosts can access this endpoint."

        return (request.user.is_authenticated and hasattr(request.user, 'host'))






