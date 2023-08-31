import tweepy

import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("TYp4cLHExMpW2BiY7hHPtKPZL", "ZFrzPVwCuNSh1NKk9eO0HBTNwOqOhoPrUgNaRwRKSaKvB4V0ws")
auth.set_access_token("4723366522-dIbOoPH2jxEy6K0SV7HyVH5CuwZlJUPdW2B8MnX",
                      "W7iv7K0ZF88vmGjx08HANXUp6ACilPrCyNo6iOEOhnqI0")

# Create API object
api = tweepy.API(auth)
user = api.me()
print(user.name)  # prints your name.
print(user.screen_name)
print(user.followers_count)

search = "zerotomastery"
numberOfTweets = 2


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)


# Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Usernamehere':
        print(follower.name)
        follower.follow()

# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
