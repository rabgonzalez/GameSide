from colorfield.fields import ColorField
from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    color = ColorField(blank=True, null=True, default='#ffffff')
