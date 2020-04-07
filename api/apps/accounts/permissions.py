from rest_framework import permissions
from .models import *


class IsCompany(permissions.BasePermission):

    def has_permission(self, request, view):
        safe_methods = ['POST', 'GET', 'PATCH']

        if request.user.is_anonymous():
            return False
        if CompanyTeamMember.objects.filter(
                user=request.user).exists():
            return request.method in safe_methods
