from django.db import models

# Create your models here.
class Member(models.Model):
  name = models.CharField(max_length=200,blank=True)
  value = models.CharField(max_length=500,blank=True)

  def __str__(self):
    return self.name
  
class Member(models.Model):
  name = models.CharField(max_length=200,blank=True)
  value = models.CharField(max_length=500,blank=True)

  def __str__(self):
    return self.name