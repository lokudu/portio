import tweepy

import time

# Authenticate to Twitter
auth = tweepy.OAuthHandler("TYp4cLHExMpW2BiY7hHPtKPZL", "ZFrzPVwCuNSh1NKk9eO0HBTNwOqOhoPrUgNaRwRKSaKvB4V0ws")
auth.set_access_token("4723366522-dIbOoPH2jxEy6K0SV7HyVH5CuwZlJUPdW2B8MnX",
                      "W7iv7K0ZF88vmGjx08HANXUp6ACilPrCyNo6iOEOhnqI0")

# Create API object
api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# Generous Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name =='GaluakMajak':
        follower.follow()
        break
