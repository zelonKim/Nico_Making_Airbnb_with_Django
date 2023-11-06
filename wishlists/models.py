from django.db import models
from common.models import CommonModel

class Wishlist(CommonModel):
    name=models.CharField(max_length=150)
    rooms = models.ManyToManyField("rooms.Room", related_name="whishlists")
    experiences = models.ManyToManyField("experiences.Experience", related_name="whishlists")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="whishlists")

    def __str__(self):
        return self.name