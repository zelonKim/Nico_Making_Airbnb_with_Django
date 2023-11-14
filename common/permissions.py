from strawberry.types import Info
import typing
from strawberry.permission import BasePermission


class OnlyLoggedIn(BasePermission):
    message = "You are not logged in"  # shows the message when 'has_permission()' returns False 

    def has_permission(self, source: typing.Any, info: Info):
       return info.context.request.user.is_authenticated