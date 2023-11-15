import strawberry
import typing
from . import types
from . import queries
from common.permissions import OnlyLoggedIn

        
@strawberry.type
class Query:
    all_rooms: typing.List[types.RoomType] = strawberry.field(resolver=queries.get_all_rooms, permission_classes=[OnlyLoggedIn])
    room: typing.Optional[types.RoomType] = strawberry.field(resolver=queries.get_room) 
    # typing.Optional[타입명]: 선택 타입으로 만들어줌.