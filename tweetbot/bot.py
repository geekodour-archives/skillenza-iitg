import tweepy
from random import randint

from tweetbot.models import (ExtractedUser, ExtractedTweets)

# env these later
auth = tweepy.OAuthHandler('5pRr9RthPT38WE6erPYwCUZ7T', '7XQf3wrzg2K8DTbli4XH0Gw8EDwU1lvGkQyLg6LwXTu3pJc0Sy')
auth.set_access_token('1513607755-BjVvj6iPFSoLZeWwGAK3L5KbR2Hol3RCCB7pbWF', 'aSd8PxSzViBcgJeueLBzYRqosIKa6tR6ObIp1Zud4k6OT')

api = tweepy.API(auth)

class TweetBot():

    @staticmethod
    def random_follow():
        following = api.friends_ids(item=2)
        userid = following[randint(0,2)]
        friends_friends = api.friends_ids(userid,items=5)
        for friend in friends_friends:
            # call tensorflow true false here
            # if true, follow
            user = ExtractUser.objects.filter(userid=friend)
            print(user)

    @staticmethod
    def get_last_10_tweets():
        '''last_10_tweets_for_each_following_user'''
        following = api.friends_ids(item=2)
        # filter following by checking if it used that id
        # in last two hours

        #for follower in tweepy.Cursor(api.followers).items():
        #    pass


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

class MyStreamListener2(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

bot = TweetBot()
bot.random_follow()
#myStreamListener = MyStreamListener()
#myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
#myStream.filter(track=['#Microsoft'])

#myStreamListener2 = MyStreamListener2()
#myStream2 = tweepy.Stream(auth = api.auth, listener=myStreamListener2)
#myStream2.filter(track=['#Python'])
