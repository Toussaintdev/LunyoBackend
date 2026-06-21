from rest_framework import permissions

# a utiliser uniquement lorsque l'objet est User
class IsSelfOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj or request.user.is_staff
    

# a utiliser uniquement lorsque l'objet est en relation avec User

class IsSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user