from django.db import models
from common.models import CommonModel

class Category(CommonModel):

    class CatgoryKindChoices(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=15, choices=CatgoryKindChoices.choices)

    def __str__(self):
        return f"{self.kind.title()}: {self.name}"

    class Meta:
         verbose_name_plural = "Categories" 
