import tweepy
import time
import random
from tweepy import OAuthHandler


print ("testing")
counter = 1
CONSUMER_KEY = 'b3kZUBrVmSE17F53nvzPf6kPs'
CONSUMER_SECRET = 'mb198b688QxQ4gUGZ8pJQChzB61fhEpY5ksgfzvOMQ9j32AbIz' 
ACCESS_KEY = '1304205786055286784-yU9TocJlk35CTcGvCwtjbjTcfCbQr2'
ACCESS_SECRET = '0E1OjyLqsqyCaT9cVXBFaPP9AWz03m5jFuJ6PWDVpix87'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

print(api)

target = "mhovakimian"
mentions = api.home_timeline()

for mention in mentions:
   print(str(mention.id))
 
FILE_NAME = 'last_seen_id.txt'    

def retriev_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id
    
def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return 
 
 
last_seen_id = retriev_last_seen_id(FILE_NAME)

def reply_to_tweets():

    counter = random.randint(1,1000)
    api.update_status('@'+target +" Gyot Es!!!" +str(counter))
    
while True:
    reply_to_tweets()
    time.sleep(1)
