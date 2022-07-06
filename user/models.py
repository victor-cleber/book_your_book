from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=64)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
