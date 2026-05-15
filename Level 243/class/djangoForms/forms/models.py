from django.db import models

# Create your models here.
class newModel(models.Model):
  name = models.CharField(max_length=50)
  surname = models.CharField(max_length=50)
  age = models.IntegerField(default=0)
  email = models.EmailField(max_length=70)
  password = models.CharField(max_length=120)