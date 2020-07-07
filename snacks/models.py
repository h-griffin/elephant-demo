from django.db import models

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=64)

    def __Str__(self):
        return self.name[:16]  # [:16] new limit from 64