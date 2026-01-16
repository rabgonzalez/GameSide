from django.db import models


class Platform(models.Model):
    name = models.CharField(unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(
        blank=True, null=True, upload_to='platforms/logos/', default='platforms/logos/default.png'
    )
