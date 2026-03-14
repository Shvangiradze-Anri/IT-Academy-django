from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):

    SPICINESS_LEVELS = [
        (1, "1 - Mild"),
        (2, "2"),
        (3, "3 - Medium"),
        (4, "4"),
        (5, "5 - Very Spicy"),
    ]

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    image = models.URLField(blank=True)   

    spiciness = models.IntegerField(choices=SPICINESS_LEVELS, default=1)

    vegetarian = models.BooleanField(default=False)

    contains_nuts = models.BooleanField(default=False)

    def __str__(self):
        return self.name