# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:38:12 2020

@author: saura
"""
import tweepy
import time

auth = tweepy.OAuthHandler('qGsjACs7NaMLamWCu4Sr37M5f', '1VPs4pCVwtSvSDIA26xt6agHoUdvYY86I3jAuGOaeob0szgr6R')
auth.set_access_token('4723366522-O1Eo0mT3e8204hL2EdzVo0sBHPbOxB4dC9e3aBl', 'hsmpYWnv5hEYwSaXZyXSsytS9XzJSBTQc1VoEPIGFxWXp')

api = tweepy.API(auth)

user = api.me()
print(user)     # it gives all the details, like name, scree_name, location, and various other info.
print(user.name)  # prints your name.
print(user.screen_name)
print(user.followers_count)

search = "bitcoin"
numberOfTweets = 2


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()

        except tweepy.RateLimitError:
            print("Sleeping now....")
            time.sleep(10)  # sleeps for 10 secs


# for follower in limit_handle(tweepy.Cursor(api.followers).items()):
#     print(follower.name)
#     if follower.name == 'Usernamehere':
#         print(follower.name)
#         follower.follow()


for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        tweet.retweet()
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
