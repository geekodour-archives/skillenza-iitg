from django.shortcuts import render
from django.views import View

from apps.tweetbot.models import ExtractedUser, ExtractedTweet

class HomeView(View):
    def get(self, request):
        currentTweets = ExtractedTweet.objects.all()
        return render(request, 'core/index.html', {'tweets':currentTweets})
