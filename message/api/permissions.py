from rest_framework import permissions
from django.contrib.auth import authenticate

class IsMessageSenderOrReceiver(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user == obj.sender or request.user == obj.receiver:
            return True