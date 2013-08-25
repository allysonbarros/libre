from __future__ import absolute_import

from rest_framework import permissions

from .models import SourceDataVersion, Source


class IsAllowedGroupMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, SourceDataVersion):
            obj = obj.source

        for group in obj.allowed_groups.all():
            if group in request.user.groups.all():
                return True

        return False
