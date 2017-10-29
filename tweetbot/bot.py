import tweepy

# env these later
auth = tweepy.OAuthHandler('5pRr9RthPT38WE6erPYwCUZ7T', '7XQf3wrzg2K8DTbli4XH0Gw8EDwU1lvGkQyLg6LwXTu3pJc0Sy')
auth.set_access_token('1513607755-BjVvj6iPFSoLZeWwGAK3L5KbR2Hol3RCCB7pbWF', 'aSd8PxSzViBcgJeueLBzYRqosIKa6tR6ObIp1Zud4k6OT')

api = tweepy.API(auth)

class TweetBot():
    @staticmethod
    def search_if_someone_to_follow():
        user = api.get_user('geekodour')
        print(user.followers_count)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

class MyStreamListener2(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

#myStreamListener = MyStreamListener()
#myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
#myStream.filter(track=['#Microsoft'])

myStreamListener2 = MyStreamListener2()
myStream2 = tweepy.Stream(auth = api.auth, listener=myStreamListener2)
myStream2.filter(track=['#Python'])
