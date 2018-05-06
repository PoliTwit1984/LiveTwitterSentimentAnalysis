import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob

consumer_key='Es9AMEhHF5c2varZvODvUPtNk'
consumer_secret='Xri426N3Z4fy9r60c1rreUOLapseBsFuSXz23XuO3vzEsWSqnu'
access_token='4807340682-0pkgd2glkaSJNGBQd2eldigV2z7WrKO8CJxLunq'
access_secret='jcFavm1i8qjJTrcMpDOpP7fCUY3gackWfWWOD6Tiychsj'

auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api=tweepy.API(auth)

class MyListener(StreamListener):

    def on_data(self,data):
        try:
            all_data=json.loads(data)
            tweet=all_data["text"]
            txtblb=TextBlob(tweet).sentiment
            print(tweet,txtblb.polarity,txtblb.subjectivity)
            if(txtblb.subjectivity*100>=60):
                output=open("bb2.txt","a")
                output.write(str(txtblb.polarity))
                output.write('\n')
                output.close()
                return True
        except BaseException as e:
                print("error on_data: %s"% str(e))
        return True

    def on_error(self,status):
        print (status)
        return True
twitter_stream=Stream(auth,MyListener())
twitter_stream.filter(track=['AMU','WeStandWithAMU'])




