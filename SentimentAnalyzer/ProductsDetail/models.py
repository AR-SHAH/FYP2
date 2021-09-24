from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related


class Product(models.Model):
    product_id = models.CharField(max_length=50, db_index=True)


class Review(models.Model):
    product_id = models.ForeignKey(
        Product, related_name='reviews', on_delete=CASCADE)
    reviews = models.CharField(max_length=8000)
    polarity = models.CharField(max_length=8)
    score = models.PositiveIntegerField()

  