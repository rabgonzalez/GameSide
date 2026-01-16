import uuid

from django.contrib.auth import get_user_model
from django.db import models


class Order(models.Model):
    class Status(models.IntegerChoices):
        INITIATED = 1
        CONFIRMED = 2
        PAID = 3
        CANCELLED = -1

    status = models.SmallIntegerField(choices=Status, default=Status.INITIATED)
    key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(get_user_model(), related_name='orders', on_delete=models.CASCADE)
    games = models.ManyToManyField(
        'games.Game',
        blank=True,
        related_name='orders',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
