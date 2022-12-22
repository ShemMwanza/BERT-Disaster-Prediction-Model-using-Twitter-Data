import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

from datetime import date

# api key
api_key = ''
# api secret key
api_secret_key = ''
# access token
access_token = ''
# access token secret
access_token_secret = ''

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
        for tweet in tweepy.Cursor(api.search_tweets,q=text_query, until=date_since, 
        count=100,lang="en",
        geocode="-1.3032641,36.8263841,300km").items(count):
            print(tweet.text)
            # Storing tweets
            tweets.append({'tweet_text': tweet.text,
                            'tweet_location' : tweet.user.location})
        return pd.DataFrame.from_dict(tweets)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)