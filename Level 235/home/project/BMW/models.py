from django.db import models

# Create your models here.
class BMWS(models.Model):
  title = models.CharField(max_length=50)
  desc = models.CharField(max_length=50)
  price = models.CharField(default=0)
  img = models.CharField(default="")