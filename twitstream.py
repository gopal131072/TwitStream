from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import config

file = open("location.txt","w",encoding="utf-8")

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]

        username = all_data["user"]["screen_name"]

        location = all_data["user"]["location"]

        if location is not None:
            print((tweet + " : " + location + "\n"))
            file.write(location + "\n")
        else:
            print((tweet + " : " + "No location supplied\n"))
            file.write("No location supplied\n")
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(config.ckey, config.csecret)
auth.set_access_token(config.atoken, config.asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["rain","damp"])

file.close()
