# import tweepy
# import time
# import pandas as pd
# pd.set_option('display.max_colwidth', 1000)

# # api key
# api_key = "Enter API Key"
# # api secret key
# api_secret_key = "Enter API Secret Key"
# # access token
# access_token = "Enter Access Token"
# # access token secret
# access_token_secret = "Enter Access Token Secret"

# authentication = tweepy.OAuthHandler(api_key, api_secret_key)
# authentication.set_access_token(access_token, access_token_secret)
# api = tweepy.API(authentication, wait_on_rate_limit=True)

# def get_Tweets(text_query):
#     # list to store tweets
#     tweets_list = []
#     # no of tweets
#     count = 100
#     try:
#         # Pulling individual tweets from query
#         for tweet in api.search(q=text_query, count=count):
#             print(tweet.text)
#             # Adding to list that contains all tweets
#             tweets_list.append({'created_at': tweet.created_at,
#                                 'tweet_id': tweet.id,
#                                 'tweet_text': tweet.text})
#         return pd.DataFrame.from_dict(tweets_list)

#     except BaseException as e:
#         print('failed on_status,', str(e))
#         time.sleep(3)

import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

from datetime import date

# api key
api_key = '12CsSFa16GkKLcuACIIknYOJ6'
# api secret key
api_secret_key = 'KtpkZUwjegQt0BlMUsGgLz5mmgg4Xdit5RLmlTA9LgY2oSiO3D'
# access token
access_token = '563617283-WUJZqsgD3kqVUCQVmtQe7EWkHwa4w3kMeDXVwOzn'
# access token secret
access_token_secret = 'OG80dsnJwE1QV32gcdazHQeuEh8ZQRzgzwQNrw3Sc8VoQ'

authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

# function for getting Tweets
def fetch_Tweets(text_query):
    tweets = []
    #number of tweets to be fetched
    count = 100
    date_since = date.today()
    try:
        # Fetching tweets individually
        for tweet in tweepy.Cursor(api.search_tweets,q=text_query, until=date_since, count=100,lang="en",geocode="-1.3032641,36.8263841,300km").items(count):
            print(tweet.text)
            # Storing tweets
            tweets.append({'tweet_text': tweet.text,
                            'tweet_location' : tweet.user.location})
        return pd.DataFrame.from_dict(tweets)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)