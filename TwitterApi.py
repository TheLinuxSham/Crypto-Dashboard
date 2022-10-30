# Importieren der libraries
import re
import pandas as pd
import tweepy as tw

# Anmeldedaten für Twitter-API
consumer_key = 'TNOgZp2ljAxdE0ILwsH3lHzua'
consumer_secret = 'BRBRgJBYI0RzM2gm473CyCIpklSlXO2JGLd1iwQkX5DesxAiPs'
access_token = '1517887559497654273-B6ZZcg1ib6DpnCmHFQ7GnZz6rXNIyf'
access_token_secret = 'nsr4TFA9tcTOALFFxkGNTqrjE3sQWRqVNMrOgwjMgInXD'

#anmelden auf Twitter API
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#max anzahl festlegen von tweets
limit = 5
#Bitcoin auslesen
post1 = tw.Cursor(api.search_tweets, q='Bitcoin -filter:retweets', lang='en', count=5, tweet_mode='extended').items(
    limit)

#tabellen format
btctw_df = pd.DataFrame([tweet.full_text for tweet in post1], columns=['Tweets'])


# Methode zum Rausfiltern der Sonderzeichen und ungewünschten Elementen in den Tweets
def clean(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'RT[\s]+', '', text)
    text = re.sub(r'https?:\/\/\S+', '', text)
    return text

#panda tabelle neu angelegt/ersetzen mit sonderzeichenfilterung
btctw_df['Tweets'] = btctw_df['Tweets'].apply(clean)
btctw_df['Währung'] = 'Bitcoin (BTC)'

# ETH auslesen
post2 = tw.Cursor(api.search_tweets, q='Ethereum -filter:retweets', lang='en', count=5,
                  tweet_mode='extended').items(limit)

ethtw_df = pd.DataFrame([tweet.full_text for tweet in post2], columns=['Tweets'])

ethtw_df['Tweets'] = ethtw_df['Tweets'].apply(clean)
ethtw_df['Währung'] = 'Ethereum (ETH)'

# BNB auslesen
post3 = tw.Cursor(api.search_tweets, q='Binance -filter:retweets', lang='en', count=5, tweet_mode='extended').items(
    limit)

bnbtw_df = pd.DataFrame([tweet.full_text for tweet in post3], columns=['Tweets'])

bnbtw_df['Tweets'] = bnbtw_df['Tweets'].apply(clean)
bnbtw_df['Währung'] = 'Binance Coin (BNB)'

# Ripple auslesen
post4 = tw.Cursor(api.search_tweets, q='Ripple -filter:retweets', lang='en', count=5, tweet_mode='extended').items(
    limit)

xrptw_df = pd.DataFrame([tweet.full_text for tweet in post4], columns=['Tweets'])

xrptw_df['Tweets'] = xrptw_df['Tweets'].apply(clean)
xrptw_df['Währung'] = 'Ripple (XRP)'

# ADA auslesen
post5 = tw.Cursor(api.search_tweets, q='Cardano -filter:retweets', lang='en', count=5, tweet_mode='extended').items(
    limit)

adatw_df = pd.DataFrame([tweet.full_text for tweet in post5], columns=['Tweets'])

adatw_df['Tweets'] = adatw_df['Tweets'].apply(clean)
adatw_df['Währung'] = 'Cardano (ADA)'

# SOL auslesen
post6 = tw.Cursor(api.search_tweets, q='Solana -filter:retweets', lang='en', count=5, tweet_mode='extended').items(
    limit)

soltw_df = pd.DataFrame([tweet.full_text for tweet in post6], columns=['Tweets'])

soltw_df['Tweets'] = soltw_df['Tweets'].apply(clean)
soltw_df['Währung'] = 'Solana (SOL)'

# DOT auslesen
post7 = tw.Cursor(api.search_tweets, q='Polkadot -filter:retweets', lang='en', count=5,
                  tweet_mode='extended').items(limit)

dottw_df = pd.DataFrame([tweet.full_text for tweet in post7], columns=['Tweets'])

dottw_df['Tweets'] = dottw_df['Tweets'].apply(clean)
dottw_df['Währung'] = 'Polkadot (DOT)'

# Doge auslesen
post8 = tw.Cursor(api.search_tweets, q='Dogecoin -filter:retweets', lang='en', count=5,
                  tweet_mode='extended').items(limit)

dogetw_df = pd.DataFrame([tweet.full_text for tweet in post8], columns=['Tweets'])

dogetw_df['Tweets'] = dogetw_df['Tweets'].apply(clean)
dogetw_df['Währung'] = 'Dogecoin (DOGE)'

# TRX auslesen
post9 = tw.Cursor(api.search_tweets, q='Tron -filter:retweets', lang='en', count=5, tweet_mode='extended').items(
    limit)

trontw_df = pd.DataFrame([tweet.full_text for tweet in post9], columns=['Tweets'])

trontw_df['Tweets'] = trontw_df['Tweets'].apply(clean)
trontw_df['Währung'] = 'Tron (TRX)'

# AVAX auslesen
post10 = tw.Cursor(api.search_tweets, q='Avalanche -filter:retweets', lang='en', count=5,
                   tweet_mode='extended').items(limit)

avatw_df = pd.DataFrame([tweet.full_text for tweet in post10], columns=['Tweets'])

avatw_df['Tweets'] = avatw_df['Tweets'].apply(clean)
avatw_df['Währung'] = 'Avalanche (AVAX)'

#kombiniert alle krypthodaten das sie auf selbe variable reagieren
y = [btctw_df, ethtw_df, bnbtw_df, adatw_df, xrptw_df, soltw_df, dottw_df, dogetw_df, trontw_df, avatw_df]
twitterdata_df = pd.concat(y)


# Methode zur Übergabe der Daten an das Hauptptogramm
def pd_getApi2():
    return twitterdata_df


def testing_dfApi2():
    return btctw_df
