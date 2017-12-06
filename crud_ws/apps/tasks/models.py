import uuid

from django.db import models


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey('accounts.User', null=True, blank=True)
    expiration_date = models.DateField()
    title = models.CharField(max_length=41)
    description = models.TextField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
