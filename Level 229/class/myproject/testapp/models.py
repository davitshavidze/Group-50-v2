from django.db import models

# Create your models here.

class activity(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=50)
  price = models.IntegerField(default=0)
  img = models.models.ImageField()