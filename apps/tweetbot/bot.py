import tweepy
from datetime import datetime, timedelta
from random import randint

from .models import ExtractedUser, ExtractedTweet
time_threshold = datetime.now() - timedelta(hours=1)

# env these later
auth = tweepy.OAuthHandler('5pRr9RthPT38WE6erPYwCUZ7T', '7XQf3wrzg2K8DTbli4XH0Gw8EDwU1lvGkQyLg6LwXTu3pJc0Sy')
auth.set_access_token('1513607755-BjVvj6iPFSoLZeWwGAK3L5KbR2Hol3RCCB7pbWF', 'aSd8PxSzViBcgJeueLBzYRqosIKa6tR6ObIp1Zud4k6OT')

api = tweepy.API(auth)

class TweetBot():

    def get_last_10_tweets(self,user):
        ''' last_10_tweets_for_user '''
        tweets  = api.user_timeline(str(user))
        for tweet in tweets:
            #tweetitem = ExtractedTweet.objects.filter(tweetid=friend,created__lt=time_threshold)
            print(tweet)

    def random_follow(self):
        following = api.friends_ids(item=4)
        userid = following[randint(0,4)]
        friends_friends = api.friends_ids(userid,items=5)
        for friend in friends_friends:
            print('poop')
            api.create_friendship(str(friend)) # tensorflow model not deployed, so follow all
            user = ExtractedUser.objects.filter(userid=friend,modified__lt=time_threshold)
            if not user:
                ExtractedUser.objects.create(userid=friend)
                print('friend:',friend)
                self.get_last_10_tweets(friend)
            else:
                self.get_last_10_tweets(friend)
                # update created at todo

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

class MyStreamListener2(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

#bot = TweetBot()
#bot.random_follow()
#myStreamListener = MyStreamListener()
#myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
#myStream.filter(track=['#Microsoft'])

#myStreamListener2 = MyStreamListener2()
#myStream2 = tweepy.Stream(auth = api.auth, listener=myStreamListener2)
#myStream2.filter(track=['#Python'])
