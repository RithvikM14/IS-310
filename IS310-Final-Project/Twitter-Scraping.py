import numpy as np  # Linear algebra
import pandas as pd  # Data processing, CSV file I/O (e.g. pd.read_csv)
import tweepy as tw  # To extract Twitter data
from tqdm import tqdm  # For progress bar
# Twitter API credentials
consumer_api_key = 'your_consumer_api_key'
consumer_api_secret = 'your_consumer_api_secret'
# OAuth authentication
auth = tw.OAuthHandler(consumer_api_key, consumer_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)
# Define the search query
search_words = "#ipl2021 -filter:retweets"
date_since = ""
date_until = ""
# Collect tweets
tweets = tw.Cursor(api.search_tweets, q=search_words, lang="en", since=date_since,until=date_until).items(7500)
# Prepare to collect tweets
tweets_list = []
# Loop through each tweet
for tweet in tqdm(tweets):
    hashtags = [hashtag['text'] for hashtag in tweet.entities['hashtags']]
    tweets_list.append({
        'user_name': tweet.user.name,
        'user_location': tweet.user.location,
        'user_description': tweet.user.description,
        'user_created': tweet.user.created_at,
        'user_followers': tweet.user.followers_count,
        'user_friends': tweet.user.friends_count,
        'user_favourites': tweet.user.favourites_count,
        'user_verified': tweet.user.verified,
        'date': tweet.created_at,
        'text': tweet.text,
        'hashtags': hashtags if hashtags else None,
        'source': tweet.source,
        'is_retweet': tweet.retweeted
    })
# Create DataFrame
tweets_df = pd.DataFrame(tweets_list)
# Save the DataFrame to a CSV file
tweets_df.to_csv('ipl_2021_tweets.csv', index=False)
print(f"New tweets retrieved: {len(tweets_df)}")
