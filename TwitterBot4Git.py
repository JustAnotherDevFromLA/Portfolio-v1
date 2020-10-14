#!/usr/bin/env python

import tweepy
import time
import random
import logging
import os
import json
from tweepy import OAuthHandler

CONSUMER_KEY = ''
CONSUMER_SECRET = '' 
ACCESS_KEY = ''
ACCESS_SECRET = ''


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

logger = logging.getLogger()
target = "@" 

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        
    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            return
        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            try:
                tweet.retweet()
            except Exception as e:
               logger.error("Error on fav and retweet", exc_info=True)
    
    def on_exception(self, exception):
        print(exception)
        return

    def on_error(self, status):
        logger.error(status)

def retweetLiker(keywords):
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])

    
    
while True:
    print("Tweeting...")
    try: 
        print("Retweeting and Fav Posts Now")
        retweetLiker(["YourHashtags"]) 
       
        break
    
    except tweepy.TweepError:
        print("Error")     
