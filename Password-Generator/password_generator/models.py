from django.db import models


class Password(models.Model):
    length = models.PositiveIntegerField()
    value = models.CharField(max_length=128)
