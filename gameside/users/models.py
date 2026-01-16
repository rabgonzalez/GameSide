import uuid

from django.contrib.auth import get_user_model
from django.db import models


class Token(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='token', on_delete=models.CASCADE)
    key = models.UUIDField(default=uuid.uuid4, blank=True, null=True, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
