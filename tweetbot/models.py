from django.db import models
from core.models import Category

# 3rd party library imports
from model_utils.models import TimeStampedModel

class ExtractedTweet(models.Model, TimeStampedModel):
     snippet = models.CharField(max_length=80)
     categories = models.ManyToManyField(Category,related_name='tweets')
     tweetid = models.CharField(max_length=80)

class ExtractedUser(models.Model, TimeStampedModel):
     categories = models.ManyToManyField(Category,related_name='tweets')
     userid = models.CharField(max_length=80)

