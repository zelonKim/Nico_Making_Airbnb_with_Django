from django.urls import path
from .import views


"""
urlpatterns = [
    path("", views.see_all_rooms), #  If the user access "rooms/", Django executes 'see_all_rooms()'
    path("<int:room_id>", views.see_one_room), #  If the user access "rooms/1", Django executes 'see_one_room(room_id=1)'   # <parameter`s type : parameter`s name>: If the path matches the parameter`s type, View function takes the parameter`s name with the path`s value
] 
"""


urlpatterns = [
    path("", views.Rooms.as_view()),
    path("<int:pk>", views.RoomDetail.as_view()),
    path("<int:pk>/reviews", views.RoomReviews.as_view()),
    path("<int:pk>/photos", views.RoomPhotos.as_view()),
    path("<int:pk>/bookings", views.RoomBookings.as_view()),
    path("amenities/", views.Amenities.as_view()),
    path("amenities/<int:pk>", views.AmenitiyDetail.as_view())
]