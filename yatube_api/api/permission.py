from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super().has_permission(request, view)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пермишен, позволяющий только владельцу объекта редактировать или удалять его.
    Другим пользователям разрешено только просматривать объект.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешено просматривать любому пользователю (GET-запросы)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешено редактировать или удалять только владельцу объекта
        return obj.author == request.user


class IsOwnerOrModeratorOrReadOnly(permissions.BasePermission):
    """
    Пермишен, позволяющий владельцу объекта и модератору редактировать или удалять его.
    Другим пользователям разрешено только просматривать объект.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешено просматривать любому пользователю (GET-запросы)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешено редактировать или удалять владельцу объекта или модератору
        return obj.author == request.user or request.user.role == 'moderator'


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Пермишен, позволяющий администратору полный доступ к объекту.
    Другим пользователям разрешено только просматривать объект.
    """

    def has_permission(self, request, view):
        # Разрешено просматривать любому пользователю (GET-запросы)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешено только администратору
        return request.user.role == 'admin'


class IsSuperuser(permissions.BasePermission):
    """
    Пермишен, проверяющий, является ли пользователь суперпользователем.
    Требуется для права администратора.
    """

    def has_permission(self, request, view):
        return request.user.is_superuser