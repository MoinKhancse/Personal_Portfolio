from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class contract(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    sub=models.TextField()
    message=models.TextField()
