import requests
import tweepy
import random
from pytz import timezone
from datetime import datetime
import sys


HASH_TAGS = "#quoteoftheday #motivation #MotivationalQuotes"

CONSUMER_KEY = sys.argv[1]
CONSUMER_SECRET = sys.argv[2]
TOKEN = sys.argv[3]
TOKEN_SECRET = sys.argv[4]
print(TOKEN_SECRET)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(TOKEN, TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)



url = "https://type.fit/api/quotes"

data = requests.get(url).json()
quote_object = random.choice(data)

qoute = quote_object['text']
qoute_author = quote_object['author']

tweet = f"{qoute}\n\n{qoute_author}\n{HASH_TAGS}"

print(tweet)

while True:
    current_time = datetime.now(timezone("Asia/Kolkata"))
    if current_time.hour == 5 or (current_time.hour == 15 or current_time.minute == 30):
        print("Making tweet")
        api.update_status(tweet)
        break



