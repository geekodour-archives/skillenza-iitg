from django.contrib import admin
from .models import ExtractedUser, ExtractedTweet
admin.site.register([ExtractedUser, ExtractedTweet])

# Register your models here.
