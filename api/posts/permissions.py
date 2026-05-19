from rest_framework.permissions import BasePermission, SAFE_METHODS

# for authenticated admin user
class ReadOnlyorAdmin(BasePermission):
    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS request
        if request.method in SAFE_METHODS:
            return True
        
        # required authentication and most be admin for
        # POST, DELETE AND PUT/PATCH request
        return request.user and request.user.is_superuser


# for authenticated user only
class ReadOnlyorAuthenticated(BasePermission):
    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS request
        if request.method in SAFE_METHODS:
            return True
        
        # required authentication and most be admin for
        # POST, DELETE AND PUT/PATCH request
        return request.user and request.user.is_authenticated  