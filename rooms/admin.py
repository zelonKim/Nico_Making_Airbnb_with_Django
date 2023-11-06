from django.contrib import admin
from .models import Room, Amenity


""" 
@admin.action(description="Set all prices to zero")
def reset_prices(models_admin, request, queryset):
    print(models_admin) # rooms.RoomAdmin
    print(request) # <WSGIRequest: POST '/admin/rooms/room/'>
    print(queryset) # [<Room: Apt>]
"""

@admin.action(description="Set all prices to zero")
def reset_prices(models_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)
   
    list_display = (
        "name",
        "price",
        "kind",
        "owner",
        "created_at",
        "total_amenities",
        "rating"
    )

    list_filter = (
        "country",
        "city",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )

    search_fields=("name", "^price", "=city", "owner__username")




@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )

