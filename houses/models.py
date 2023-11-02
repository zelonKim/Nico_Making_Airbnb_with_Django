from django.db import models

class House(models.Model):
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(verbose_name='price', help_text="Positive Numbers Only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True, verbose_name="Pets allowed?" ,help_text="Does this house allows pets?")

    def __str__(self):
        return self.name