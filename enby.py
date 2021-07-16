import tweepy
import os
import requests
import string
import random
import time 

def twitter_api():
  twitter_api_key = os.environ["twitter_api_key"]
  twitter_api_secret = os.environ["twitter_api_secret"]
  twitter_access_token = os.environ["twitter_access_token"]
  twitter_access_secret = os.environ["twitter_access_secret"]

  auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
  auth.set_access_token(twitter_access_token, twitter_access_secret)

  return tweepy.API(auth)

def get_random_word():
  url = "https://wordsapiv1.p.rapidapi.com/words/"
  parts_of_speech = ["noun","verb","adjective"]
  random_pos = random.choice(parts_of_speech)
  letters = list(string.ascii_lowercase)
  random_letter = random.choice(letters)
  letter_pattern = f'^{random_letter}' + '+\\w{3,10}'

  # frequencymin determins commonality of the word
  # make is around 8, so I went for fairly common words
  querystring = {"limit":"100","partofspeech":random_pos,"letterPattern":letter_pattern,"frequencymin":"7.5"}

  headers = {
      'x-rapidapi-key': os.environ["dictionary_api_key"],
      'x-rapidapi-host': os.environ["dictionary_api_host"]
      }

  response = requests.request("GET", url, headers=headers, params=querystring)

  return {
    "pos": random_pos,
    "word": random.choice(response.json()['results']['data'])
  }

def make_sentence():
  enby = ["enby", "non-binary"]
  word = get_random_word()

  # sentence order and term choice depends on word part of speech
  if word["pos"] == "adjective":
    return word["word"] + " " + enby[0]
  elif word["pos"] == "noun":
    return enby[1] + " " + word["word"]
  else:
    return random.choice(enby) + " "  + word["word"]

def tweet():
  api = twitter_api()
  sentence = make_sentence()
  status = api.update_status(sentence)
  print('tweeted ' + status.id_str + ": " + sentence)

# tweet every half hour
INTERVAL = 60 * 30 

while True:
  tweet()
  time.sleep(INTERVAL)