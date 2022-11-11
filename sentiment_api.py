import pandas as pd
import tweepy as tw
from textblob import TextBlob

# imports login data and limit value for API
import user_data as user_d

# user data given from user_data.py
auth = tw.OAuthHandler(user_d.consumer_key, user_d.consumer_secret)
auth.set_access_token(user_d.access_token, user_d.access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
limit = user_d.limitSentiment
currency_value = user_d.currency_value

# methods to categorise the tweets
def analyse_tweets(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'


def polarity(text):
    return TextBlob(text).sentiment.polarity


def remove_characters(string):
    return string.replace(" ", "")


# list for the loop
completed_currency_list = []

# loops through the currency's list given in user_data.py for tweets
for i in currency_value:
    entity = remove_characters(i.lower())
    entity_df = i.lower() + '_df'
    entity_sentiment_df = i.lower() + '_sentiment_df'

    entity = tw.Cursor(api.search_tweets, q=f'{i} -filter:retweets', lang='en', count=limit,
                       tweet_mode='extended').items(limit)
    entity_df = pd.DataFrame([tweet.full_text for tweet in entity], columns=['Tweets'])

    entity_df['Polarity'] = entity_df['Tweets'].apply(polarity)
    entity_df['Analysis'] = entity_df['Polarity'].apply(analyse_tweets)

    positive = entity_df.Analysis.str.count('Positive').sum()
    neutral = entity_df.Analysis.str.count('Neutral').sum()
    negative = entity_df.Analysis.str.count('Negative').sum()

    entity_sentiment_df = pd.DataFrame({'Positive': [positive],
                                        'Neutral': [neutral],
                                        'Negative': [negative]})

    entity_sentiment_df['Währung'] = f'{i}'

    completed_currency_list.append(entity_sentiment_df)

# merges dataframes and clears the old one
dataframe_sentiment = pd.concat(completed_currency_list)
completed_currency_list.clear()


# method to return the dataframe to main
def get_sentiment_dataframes():
    return dataframe_sentiment
