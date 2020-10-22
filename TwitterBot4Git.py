#!/usr/bin/env python

import tweepy
import time
import random
import logging
import os
import json
from tweepy import OAuthHandler

#placeholders for the keys which are needed to interact with twitter API
CONSUMER_KEY = ''
CONSUMER_SECRET = '' 
ACCESS_KEY = ''
ACCESS_SECRET = ''

#autharize the access with twitter 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

logger = logging.getLogger()

class FavRetweetListener(tweepy.StreamListener):    #used to filter input stream from twitter
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        
    def on_status(self, tweet):         
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            return
        if not tweet.favorited: #check if the tweet isnt favorited and then favorite it 
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)  #try-catch with error handling with logger
        if not tweet.retweeted:  #check if the tweet isnt favorited and then favorite it 
            try:
                tweet.retweet()
            except Exception as e:
               logger.error("Error on fav and retweet", exc_info=True)  #try-catch with error handling with logger
    
    def on_exception(self, exception):  #used for handling autodisconnect from twitter servers 
        print(exception)
        return

    def on_error(self, status): #used for error logging 
        logger.error(status)

def retweetLiker(keywords):
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])

    
    
while True: 
    print("Tweeting...")    #make sure bot is running
    try: 
        print("Retweeting and Fav Posts Now")   
        retweetLiker(["YourHashtags"]) #call function and intput desired hashtags for filtering
        break
    
    except tweepy.TweepError:   #try catch to insure bot keeps running
        print("Error")     
