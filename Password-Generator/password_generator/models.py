from django.db import models


# Create your models here.
class GenPassword(models.Model):
    password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.password)
