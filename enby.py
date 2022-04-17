import tweepy
import os
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
  parts_of_speech = ["noun","verb","adjective","adverb"]
  random_pos = random.choice(parts_of_speech)

  word_file = open(random_pos + ".txt", "r")
  word_list = word_file.read().split(",")
  word = random.choice(word_list)

  return [random_pos, word]

def make_sentence():
  enby = ["enby", "non-binary"]
  pos, word = get_random_word()

  # sentence order depends on word part of speech
  if pos == "adjective" or pos == "adverb":
    return word + " " + random.choice(enby)
  else:
    return random.choice(enby) + " " + word

def tweet():
  api = twitter_api()
  sentence = make_sentence()
  status = api.update_status(sentence)
  print('tweeted ' + status.id_str + ": " + sentence)

tweet()
