from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    servings = models.PositiveIntegerField()

    def __str__(self):
        return self.name