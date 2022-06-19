from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.name


