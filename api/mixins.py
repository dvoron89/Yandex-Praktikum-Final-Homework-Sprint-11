from rest_framework.permissions import AllowAny, IsAdminUser


class PermissionMixin:
    def get_permissions(self):
        permission_classes = []

        if self.action in ('list', 'retrieve'):
            permission_classes = [AllowAny]

        if self.action in ('create', 'destroy', 'partial_update', 'update'):
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
