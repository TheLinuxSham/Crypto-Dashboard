import re
import pandas as pd
import tweepy as tw

# imports login data and limit value for API
import user_data as user_d

# user data given from user_data.py
auth = tw.OAuthHandler(user_d.consumer_key, user_d.consumer_secret)
auth.set_access_token(user_d.access_token, user_d.access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
limit = user_d.limitTweets
currency_value = user_d.currency_value


# method to filter unnecessary symbols
def clean_up_text(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'RT[\s]+', '', text)
    text = re.sub(r'https?:\/\/\S+', '', text)
    return text


def remove_characters(string):
    return string.replace(" ", "")


# list for the loop
completed_currency_list = []

# loops through the currency's list given in user_data.py for tweets
for i in currency_value:
    entity = remove_characters(i.lower())
    entity_df = i.lower() + '_df'
    entity = tw.Cursor(api.search_tweets, q=f'{i} -filter:retweets', lang='en', count=limit,
                       tweet_mode='extended').items(limit)
    entity_df = pd.DataFrame([tweet.full_text for tweet in entity], columns=['Tweets'])
    entity_df['Tweets'] = entity_df['Tweets'].apply(clean_up_text)
    entity_df['Währung'] = f'{i}'
    completed_currency_list.append(entity_df)

# merges dataframes and clears the old one
dataframe_twitter = pd.concat(completed_currency_list)
completed_currency_list.clear()


# method to return the dataframe to main
def get_twitter_dataframes():
    return dataframe_twitter
