from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Game(models.Model):
    class PEGI(models.IntegerChoices):
        PEGI3 = 3
        PEGI7 = 7
        PEGI12 = 12
        PEGI16 = 16
        PEGI18 = 18

    title = models.CharField(unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    cover = models.ImageField(
        upload_to='games/covers/', default='games/covers/default.png', blank=True, null=True
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField()
    released_at = models.DateField()
    pegi = models.PositiveSmallIntegerField(choices=PEGI, default=PEGI.PEGI3)
    category = models.ForeignKey(
        'categories.Category',
        related_name='games',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    platforms = models.ManyToManyField('platforms.Platform', related_name='games')


class Review(models.Model):
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.CharField()
    game = models.ForeignKey(Game, related_name='reviews', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
