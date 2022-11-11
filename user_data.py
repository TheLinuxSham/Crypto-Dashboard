"""Uses your login credentials for the Twitter APIs
you will need a Twitter development account for this"""

consumer_key = 'insert your value here'
consumer_secret = 'insert your value here'
access_token = 'insert your value here'
access_token_secret = 'insert your value here'

"""This section is for the crypto api file. You can change the key and secret key here. Also you could add new 
currencys here. Don't forget to add the keys to currencyValue, too!"""
apikey = 'X3VFoS5Q5uSPraAKgFtRnj7zWCIafeJHoR2W5qXgV5TtuO76KZwNBlAeI6HORxnd'
secretkey = 'UxjTrzwLjRxU2tt5gfLGFUppShHDUQzM0oZ3jSe55sK9anthEQOPzZFooJnINNgd'

crypto_api_list = {
    'Bitcoin': 'BTCUSDT', 'Ethereum': 'ETHUSDT', 'Binance Coin': 'BNBUSDT', 'Cardano': 'ADAUSDT', 'Ripple': 'XRPUSDT',
    'Solana': 'SOLUSDT', 'Polkadot': 'DOTUSDT', 'Dogecoin': 'DOGEUSDT', 'Avalanche': 'AVAXUSDT', 'Tron': 'TRXUSDT'}

json_request_list = {
    'btc': 'Bitcoin', 'eth': 'Ethereum', 'bnb': 'Binance Coin', 'ada': 'Cardano', 'xrp': 'Ripple',
    'sol': 'Solana', 'dot': 'Polkadot', 'doge': 'Dogecoin', 'trx': 'Tron',
    'avax': 'Avalanche'}

""""This section is for the twitter-sentiment-analysis and tweets-board. Change the number accordingly if you want to 
have more/less tweets to be processed"""
limitSentiment = 0
limitTweets = 0

currency_value = ['Bitcoin', 'Ethereum', 'Binance Coin', 'Cardano', 'Ripple', 'Solana', 'Polkadot', 'Dogecoin',
                  'Avalanche', 'Tron']


def test_crypto_key():
    return crypto_api_list
