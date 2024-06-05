from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(unique=True, max_length=100)
    description = models.TextField(max_length=255, blank=True)
    cat_img = models.ImageField(upload_to="photos/categories", blank=True)

    def __str__(self):
        return self.name
