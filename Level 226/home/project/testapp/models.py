from django.db import models

# Create your models here.
# charfield - სიმბოლოების ველი

class first_model(models.Model):
  name = models.CharField(max_length=50)
  surname = models.CharField(max_length=50)
  age = models.IntegerField(default=0)
  high_role = models.CharField(default=0)