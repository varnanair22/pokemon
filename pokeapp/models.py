from django.db import models
# Create your models here.

class pokemon(models.Model):
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=1000)
    desc = models.CharField(max_length=500, default="", blank=True)

    def __str__(self):
        return self.name


