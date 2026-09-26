from rest_framework.permissions import BasePermission

class IsSpaceOwner(BasePermission):

    def has_object_permission(self, request, view, obj):

        return obj.host.user == request.user.id







