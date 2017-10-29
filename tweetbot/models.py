from django.db import models

from core.models import Category

class ExtractedTweet(models.Model):
     snippet = models.CharField(max_length=80)
     categories = models.ManyToManyField(Category,related_name='tweets')
