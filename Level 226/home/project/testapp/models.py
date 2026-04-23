from django.db import models

# Create your models here.
# charfield - სიმბოლოების ველი

class first_model(models.Model):
  name = models.CharField(max_length=50)
  surname = models.CharField(max_length=50)
  age = models.IntegerField(default=0)
  high_role = models.CharField(default=0)
  group_name = models.CharField(default=50)

class second_model(models.Model):
  name = models.CharField(max_length=40)
  surname = models.CharField(max_length=40)
  status = models.CharField(max_length=40)
  month_mentor = models.CharField(max_length=40)

class assistants(models.Model):
  name = models.CharField(max_length=40)
  surname = models.CharField(max_length=40)
  group = models.IntegerField(default=0)
