from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import config

# The file where we'll store all the locations we get from the twitter api.

file = open("../output/location.txt","w",encoding="utf-8")

# The file where we'll store all the tweets we get from the twitter api.
newfile = open("../output/tweets.txt","w",encoding="utf-8")
class listener(StreamListener):

    def on_data(self, data):
        # The JSON return we get from the api.
        all_data = json.loads(data)
        # We need only the location technically but since I was practicing with the twitter api I got the text of the tweet to print on the screen too.
        tweet = all_data["text"]
        # The location in standard json syntax.
        location = all_data["user"]["location"]
        # Since location is customizable it can be left blank. Filtering those out.
        if location is not None:
            print((tweet + " : " + location + "\n"))
            file.write(location + "\n")
            newfile.write(tweet + "\n")
        else:
            print((tweet + " : " + "No location supplied\n"))
            file.write("No location supplied\n")
            newfile.write(tweet + "\n")
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(config.ckey, config.csecret)
auth.set_access_token(config.atoken, config.asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#FakeNews"])

file.close()
newfile.close()