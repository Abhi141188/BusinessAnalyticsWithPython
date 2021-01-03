# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:02:51 2020

@author: Abhinav
"""
#Import Libraries
import tweepy
from textblob import TextBlob

#Twitter Authentication
consumer_key = 'zGyB4DjnB32mKpKxZaF4M2PnB'
consumer_secret = 'DsV7gfgJxOBV0wgSq4UN5j3yYNOlsrSxGw2xhF7Kz0JQHeZ6AF'
access_token = '1212320988563558406-oFECPAuTKJQ7cMYGkAeptJ0R1rbu4v'
access_token_secret = '5kivnKzSVyE3B2CoT1UrHaAQ8SM7tGhSUe9ZsPd6xQSAG'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Reading data from twitter
api = tweepy.API(auth)
public_tweets = api.search('China')

#Printing the data read from twitter
for tweet in public_tweets:
    print(tweet.text)
    
#Performing Sentiment Analysis
    analysis = TextBlob(tweet.text)
    type(analysis)
    print(analysis.sentiment)
