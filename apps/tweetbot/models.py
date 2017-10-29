from django.db import models
from apps.core.models import Category

# 3rd party library imports
from model_utils.models import TimeStampedModel

#class ExtractedTweet(models.Model, TimeStampedModel):
class ExtractedTweet(TimeStampedModel, models.Model):
     snippet = models.CharField(max_length=80)
     tweet = models.CharField(max_length=200)
     categories = models.ManyToManyField(Category,related_name='tweets')
     tweetid = models.CharField(max_length=80,unique=True)

     def __str__(self):
         return self.tweetid

#class ExtractedUser(models.Model, TimeStampedModel):
class ExtractedUser(TimeStampedModel, models.Model):
     userid = models.CharField(max_length=80,unique=True)

     def __str__(self):
         return self.userid
