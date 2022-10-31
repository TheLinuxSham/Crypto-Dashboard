# Importieren der libraries
import pandas as pd
import tweepy as tw
from textblob import TextBlob

# Anmeldedaten für Twitter-API
consumer_key = 'insert your key value here'
consumer_secret = 'insert your key value here'
access_token = 'insert your key value here'
access_token_secret = 'insert your key value here'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


# 5 Twitter Sentiment

# Methode zum Kategorisieren der Tweets in positiv, negativ und neutral
def getAnalysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'


# BTC
limit = 50
btc1 = tw.Cursor(api.search_tweets, q='Bitcoin -filter:retweets', lang='en', count=50, tweet_mode='extended').items(
    limit)
btcs_df = pd.DataFrame([tweet.full_text for tweet in btc1], columns=['Tweets'])


def polarity(text):
    return TextBlob(text).sentiment.polarity


btcs_df['Polarity'] = btcs_df['Tweets'].apply(polarity)
btcs_df['Analysis'] = btcs_df['Polarity'].apply(getAnalysis)

abtc = btcs_df.Analysis.str.count('Positive').sum()
bbtc = btcs_df.Analysis.str.count('Neutral').sum()
cbtc = btcs_df.Analysis.str.count('Negative').sum()

btcsenti_df = pd.DataFrame({'Positive': [abtc],
                            'Neutral': [bbtc],
                            'Negative': [cbtc]})

btcsenti_df['Währung'] = "Bitcoin (BTC)"

# ETH
eth1 = tw.Cursor(api.search_tweets, q='Ethereum -filter:retweets', lang='en', count=50,
                 tweet_mode='extended').items(limit)
eths_df = pd.DataFrame([tweet.full_text for tweet in eth1], columns=['Tweets'])

eths_df['Polarity'] = eths_df['Tweets'].apply(polarity)
eths_df['Analysis'] = eths_df['Polarity'].apply(getAnalysis)

aeth = eths_df.Analysis.str.count('Positive').sum()
beth = eths_df.Analysis.str.count('Neutral').sum()
ceth = eths_df.Analysis.str.count('Negative').sum()

ethsenti_df = pd.DataFrame({'Positive': [aeth],
                            'Neutral': [beth],
                            'Negative': [ceth]})

ethsenti_df['Währung'] = "Ethereum (ETH)"

# BNB
bnb1 = tw.Cursor(api.search_tweets, q='Binance -filter:retweets', lang='en', count=50, tweet_mode='extended').items(
    limit)
bnbs_df = pd.DataFrame([tweet.full_text for tweet in bnb1], columns=['Tweets'])

bnbs_df['Polarity'] = bnbs_df['Tweets'].apply(polarity)
bnbs_df['Analysis'] = bnbs_df['Polarity'].apply(getAnalysis)

abnb = bnbs_df.Analysis.str.count('Positive').sum()
bbnb = bnbs_df.Analysis.str.count('Neutral').sum()
cbnb = bnbs_df.Analysis.str.count('Negative').sum()

bnbsenti_df = pd.DataFrame({'Positive': [abnb],
                            'Neutral': [bbnb],
                            'Negative': [cbnb]})

bnbsenti_df['Währung'] = "Binance Coin (BNB)"

# ADA
ada1 = tw.Cursor(api.search_tweets, q='Cardano -filter:retweets', lang='en', count=50, tweet_mode='extended').items(
    limit)
adas_df = pd.DataFrame([tweet.full_text for tweet in ada1], columns=['Tweets'])

adas_df['Polarity'] = adas_df['Tweets'].apply(polarity)
adas_df['Analysis'] = adas_df['Polarity'].apply(getAnalysis)

aada = adas_df.Analysis.str.count('Positive').sum()
bada = adas_df.Analysis.str.count('Neutral').sum()
cada = adas_df.Analysis.str.count('Negative').sum()

adasenti_df = pd.DataFrame({'Positive': [aada],
                            'Neutral': [bada],
                            'Negative': [cada]})

adasenti_df['Währung'] = "Cardano (ADA)"

# XRP
xrp1 = tw.Cursor(api.search_tweets, q='Ripple -filter:retweets', lang='en', count=50, tweet_mode='extended').items(
    limit)
xrps_df = pd.DataFrame([tweet.full_text for tweet in xrp1], columns=['Tweets'])

xrps_df['Polarity'] = xrps_df['Tweets'].apply(polarity)
xrps_df['Analysis'] = xrps_df['Polarity'].apply(getAnalysis)

axrp = xrps_df.Analysis.str.count('Positive').sum()
bxrp = xrps_df.Analysis.str.count('Neutral').sum()
cxrp = xrps_df.Analysis.str.count('Negative').sum()

xrpsenti_df = pd.DataFrame({'Positive': [axrp],
                            'Neutral': [bxrp],
                            'Negative': [cxrp]})

xrpsenti_df['Währung'] = "Ripple (XRP)"

# SOL
sol1 = tw.Cursor(api.search_tweets, q='Solana -filter:retweets', lang='en', count=50, tweet_mode='extended').items(
    limit)
sols_df = pd.DataFrame([tweet.full_text for tweet in sol1], columns=['Tweets'])

sols_df['Polarity'] = sols_df['Tweets'].apply(polarity)
sols_df['Analysis'] = sols_df['Polarity'].apply(getAnalysis)

asol = sols_df.Analysis.str.count('Positive').sum()
bsol = sols_df.Analysis.str.count('Neutral').sum()
csol = sols_df.Analysis.str.count('Negative').sum()

solsenti_df = pd.DataFrame({'Positive': [asol],
                            'Neutral': [bsol],
                            'Negative': [csol]})

solsenti_df['Währung'] = "Solana (SOL)"

# DOT
dot1 = tw.Cursor(api.search_tweets, q='Polkadot -filter:retweets', lang='en', count=50, tweet_mode='extended').items(
    limit)
dots_df = pd.DataFrame([tweet.full_text for tweet in dot1], columns=['Tweets'])

dots_df['Polarity'] = dots_df['Tweets'].apply(polarity)
dots_df['Analysis'] = dots_df['Polarity'].apply(getAnalysis)

adot = dots_df.Analysis.str.count('Positive').sum()
bdot = dots_df.Analysis.str.count('Neutral').sum()
cdot = dots_df.Analysis.str.count('Negative').sum()

dotsenti_df = pd.DataFrame({'Positive': [adot],
                            'Neutral': [bdot],
                            'Negative': [cdot]})

dotsenti_df['Währung'] = "Polkadot (DOT)"

# Doge
doge1 = tw.Cursor(api.search_tweets, q='Dogecoin -filter:retweets', lang='en', count=50,
                  tweet_mode='extended').items(limit)
doges_df = pd.DataFrame([tweet.full_text for tweet in doge1], columns=['Tweets'])

doges_df['Polarity'] = doges_df['Tweets'].apply(polarity)
doges_df['Analysis'] = doges_df['Polarity'].apply(getAnalysis)

adoge = doges_df.Analysis.str.count('Positive').sum()
bdoge = doges_df.Analysis.str.count('Neutral').sum()
cdoge = doges_df.Analysis.str.count('Negative').sum()

dogesenti_df = pd.DataFrame({'Positive': [adoge],
                             'Neutral': [bdoge],
                             'Negative': [cdoge]})

dogesenti_df['Währung'] = "Dogecoin (DOGE)"

# TRX
trx1 = tw.Cursor(api.search_tweets, q='Tron -filter:retweets', lang='en', count=50, tweet_mode='extended').items(
    limit)
trxs_df = pd.DataFrame([tweet.full_text for tweet in trx1], columns=['Tweets'])

trxs_df['Polarity'] = trxs_df['Tweets'].apply(polarity)
trxs_df['Analysis'] = trxs_df['Polarity'].apply(getAnalysis)

atrx = trxs_df.Analysis.str.count('Positive').sum()
btrx = trxs_df.Analysis.str.count('Neutral').sum()
ctrx = trxs_df.Analysis.str.count('Negative').sum()

trxsenti_df = pd.DataFrame({'Positive': [atrx],
                            'Neutral': [btrx],
                            'Negative': [ctrx]})

trxsenti_df['Währung'] = "Tron (TRX)"

# AVAX
ava1 = tw.Cursor(api.search_tweets, q='Avalanche -filter:retweets', lang='en', count=50,
                 tweet_mode='extended').items(limit)
avas_df = pd.DataFrame([tweet.full_text for tweet in ava1], columns=['Tweets'])

avas_df['Polarity'] = avas_df['Tweets'].apply(polarity)
avas_df['Analysis'] = avas_df['Polarity'].apply(getAnalysis)

aava = avas_df.Analysis.str.count('Positive').sum()
bava = avas_df.Analysis.str.count('Neutral').sum()
cava = avas_df.Analysis.str.count('Negative').sum()

avasenti_df = pd.DataFrame({'Positive': [aava],
                            'Neutral': [bava],
                            'Negative': [cava]})

avasenti_df['Währung'] = "Avalanche (AVAX)"

z = [btcsenti_df, ethsenti_df, bnbsenti_df, adasenti_df, xrpsenti_df, solsenti_df, dotsenti_df, dogesenti_df,
     trxsenti_df, avasenti_df]
sentiment_df = pd.concat(z)


# Methode zur Übergabe der Daten an das Hauptptogramm
def pd_getApi3():
    return sentiment_df
