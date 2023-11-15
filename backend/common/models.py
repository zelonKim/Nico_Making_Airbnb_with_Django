from django.db import models

class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True) # Automatically set the field to now every time the object is saved

    class Meta:
        abstract = True  # not use as an actual Model in DataBase

