import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

def twitter_api():
  twitter_api_key = os.environ["twitter_api_key"]
  twitter_api_secret = os.environ["twitter_api_secret"]
  twitter_access_token = os.environ["twitter_access_token"]
  twitter_access_secret = os.environ["twitter_access_secret"]

  auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
  auth.set_access_token(twitter_access_token, twitter_access_secret)
  
  return tweepy.API(auth)
