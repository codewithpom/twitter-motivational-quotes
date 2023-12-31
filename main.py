import requests
import tweepy
import random
import sys


HASH_TAGS = "#motivation #MotivationalQuotes"

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

client = tweepy.Client(consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=TOKEN,
                       access_token_secret=TOKEN_SECRET)

url = "https://zenquotes.io/?api=quotes"

data = requests.get(url).json()
quote_object = random.choice(data)

qoute = quote_object['q']
qoute_author = quote_object['a']

tweet = f"{qoute}\n\n{qoute_author}\n{HASH_TAGS}"

print(tweet)

    
print("Making tweet")
client.create_tweet(text=tweet)




