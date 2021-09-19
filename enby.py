import tweepy
import os
import requests
import string
import random
import time 
# used for development
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

def get_random_word():
  url = "http://api.wordnik.com/v4/words.json/randomWord"
  api_key = os.environ["wordnik_api_key"]
  parts_of_speech = ["noun","verb","adjective","adverb"]
  random_pos = random.choice(parts_of_speech)

  # minCorpusCount determins corpus frequency of the word
  querystring = {
    "hasDictionaryDef": True,
    "includePartOfSpeech": random_pos,
    "excludePartOfSpeech": "family-name,given-name",
    "minCorpusCount": "100",
    "minLength": 3,
    "api_key": api_key
  }

  response = requests.get(url, params=querystring)

  return [random_pos, response.json()['word'].lower()]

def make_sentence():
  enby = ["enby", "non-binary"]
  pos, word = get_random_word()

  # sentence order depends on word part of speech
  if pos == "adjective" or pos == "adverb":
    return word + " " + random.choice(enby)
  else:
    return random.choice(enby) + " "  + word

def tweet():
  api = twitter_api()
  sentence = make_sentence()
  status = api.update_status(sentence)
  print('tweeted ' + status.id_str + ": " + sentence)

# tweet every hour
INTERVAL = 60 * 60

while True:
  tweet()
  time.sleep(INTERVAL)

# TO DO: set up heroku scheduler instead of using loop
