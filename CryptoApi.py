# importieren der libraries
import pandas as pd
import requests
from binance import Client

# 1 Historical Crypto-Daten
apikey = 'X3VFoS5Q5uSPraAKgFtRnj7zWCIafeJHoR2W5qXgV5TtuO76KZwNBlAeI6HORxnd'
secretkey = 'UxjTrzwLjRxU2tt5gfLGFUppShHDUQzM0oZ3jSe55sK9anthEQOPzZFooJnINNgd'

client = Client(apikey, secretkey)

# BTC
btc = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2022')
btc_df = pd.DataFrame(btc)

btc_df.columns = ['Datum', 'Open', 'High', 'Low', 'USD', 'Volume', 'Close Time',
                  'UN1', 'Anzahl', 'UN3', 'UN4', 'UN5']  # UN = Parameter die wir aktuell nicht brauchen

btc_df['Datum'] = pd.to_datetime(btc_df['Datum'] / 1000, unit='s')  # conversion zu passendem Daten-
btc_df['Close Time'] = pd.to_datetime(btc_df['Close Time'] / 1000, unit='s')  # Typ in Dataframe

btc_num = ['USD', 'Volume', 'Anzahl']  # conversion zu passendem Daten-
btc_df[btc_num] = btc_df[btc_num].apply(pd.to_numeric, axis=1)  # Typ in Dataframe

btc_df['Währung'] = "Bitcoin (BTC)"  # adden von extra column in Dataframe für spätere Zuordnung

# ETH
eth = client.get_historical_klines('ETHUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2022')
eth_df = pd.DataFrame(eth)
eth_df.columns = ['Datum', 'Open', 'High', 'Low', 'USD', 'Volume', 'Close Time',
                  'UN1', 'Anzahl', 'UN3', 'UN4', 'UN5']

eth_df['Datum'] = pd.to_datetime(eth_df['Datum'] / 1000, unit='s')
eth_df['Close Time'] = pd.to_datetime(eth_df['Close Time'] / 1000, unit='s')

eth_num = ['USD', 'Volume', 'Anzahl']
eth_df[eth_num] = eth_df[eth_num].apply(pd.to_numeric, axis=1)

eth_df['Währung'] = "Ethereum (ETH)"

# BNB
bnb = client.get_historical_klines('BNBUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2022')
bnb_df = pd.DataFrame(bnb)
bnb_df.columns = ['Datum', 'Open', 'High', 'Low', 'USD', 'Volume', 'Close Time',
                  'UN1', 'Anzahl', 'UN3', 'UN4', 'UN5']

bnb_df['Datum'] = pd.to_datetime(bnb_df['Datum'] / 1000, unit='s')
bnb_df['Close Time'] = pd.to_datetime(bnb_df['Close Time'] / 1000, unit='s')

bnb_num = ['USD', 'Volume', 'Anzahl']
bnb_df[bnb_num] = bnb_df[bnb_num].apply(pd.to_numeric, axis=1)

bnb_df['Währung'] = "Binance Coin (BNB)"

# ADA
ada = client.get_historical_klines('ADAUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2022')
ada_df = pd.DataFrame(ada)
ada_df.columns = ['Datum', 'Open', 'High', 'Low', 'USD', 'Volume', 'Close Time',
                  'UN1', 'Anzahl', 'UN3', 'UN4', 'UN5']

ada_df['Datum'] = pd.to_datetime(ada_df['Datum'] / 1000, unit='s')
ada_df['Close Time'] = pd.to_datetime(ada_df['Close Time'] / 1000, unit='s')

ada_num = ['USD', 'Volume', 'Anzahl']
ada_df[bnb_num] = ada_df[ada_num].apply(pd.to_numeric, axis=1)

ada_df['Währung'] = "Cardano (ADA)"

# XRP
xrp = client.get_historical_klines('XRPUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2022')
xrp_df = pd.DataFrame(xrp)
xrp_df.columns = ['Datum', 'Open', 'High', 'Low', 'USD', 'Volume', 'Close Time',
                  'UN1', 'Anzahl', 'UN3', 'UN4', 'UN5']

xrp_df['Datum'] = pd.to_datetime(xrp_df['Datum'] / 1000, unit='s')
xrp_df['Close Time'] = pd.to_datetime(xrp_df['Close Time'] / 1000, unit='s')

xrp_num = ['USD', 'Volume', 'Anzahl']
xrp_df[xrp_num] = xrp_df[xrp_num].apply(pd.to_numeric, axis=1)

xrp_df['Währung'] = "Ripple (XRP)"

# SOL
sol = client.get_historical_klines('SOLUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2022')
sol_df = pd.DataFrame(sol)
sol_df.columns = ['Datum', 'Open', 'High', 'Low', 'USD', 'Volume', 'Close Time',
                  'UN1', 'Anzahl', 'UN3', 'UN4', 'UN5']

sol_df['Datum'] = pd.to_datetime(sol_df['Datum'] / 1000, unit='s')
sol_df['Close Time'] = pd.to_datetime(sol_df['Close Time'] / 1000, unit='s')

sol_num = ['USD', 'Volume', 'Anzahl']
sol_df[xrp_num] = sol_df[sol_num].apply(pd.to_numeric, axis=1)

sol_df['Währung'] = "Solana (SOL)"

# DOT
dot = client.get_historical_klines('DOTUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2022')
dot_df = pd.DataFrame(dot)
dot_df.columns = ['Datum', 'Open', 'High', 'Low', 'USD', 'Volume', 'Close Time',
                  'UN1', 'Anzahl', 'UN3', 'UN4', 'UN5']

dot_df['Datum'] = pd.to_datetime(dot_df['Datum'] / 1000, unit='s')
dot_df['Close Time'] = pd.to_datetime(dot_df['Close Time'] / 1000, unit='s')

dot_num = ['USD', 'Volume', 'Anzahl']
dot_df[dot_num] = sol_df[dot_num].apply(pd.to_numeric, axis=1)

dot_df['Währung'] = "Polkadot (DOT)"

# DOGE
doge = client.get_historical_klines('DOGEUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2022')
doge_df = pd.DataFrame(doge)
doge_df.columns = ['Datum', 'Open', 'High', 'Low', 'USD', 'Volume', 'Close Time',
                   'UN1', 'Anzahl', 'UN3', 'UN4', 'UN5']

doge_df['Datum'] = pd.to_datetime(doge_df['Datum'] / 1000, unit='s')
doge_df['Close Time'] = pd.to_datetime(doge_df['Close Time'] / 1000, unit='s')

doge_num = ['USD', 'Volume', 'Anzahl']
doge_df[doge_num] = doge_df[doge_num].apply(pd.to_numeric, axis=1)

doge_df['Währung'] = "Dogecoin (DOGE)"

# TRX
trx = client.get_historical_klines('TRXUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2022')
trx_df = pd.DataFrame(trx)
trx_df.columns = ['Datum', 'Open', 'High', 'Low', 'USD', 'Volume', 'Close Time',
                  'UN1', 'Anzahl', 'UN3', 'UN4', 'UN5']

trx_df['Datum'] = pd.to_datetime(trx_df['Datum'] / 1000, unit='s')
trx_df['Close Time'] = pd.to_datetime(trx_df['Close Time'] / 1000, unit='s')

trx_num = ['USD', 'Volume', 'Anzahl']
trx_df[trx_num] = trx_df[trx_num].apply(pd.to_numeric, axis=1)

trx_df['Währung'] = "Tron (TRX)"

# AVAX
avax = client.get_historical_klines('AVAXUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2022')
avax_df = pd.DataFrame(avax)
avax_df.columns = ['Datum', 'Open', 'High', 'Low', 'USD', 'Volume', 'Close Time',
                   'UN1', 'Anzahl', 'UN3', 'UN4', 'UN5']

avax_df['Datum'] = pd.to_datetime(avax_df['Datum'] / 1000, unit='s')
avax_df['Close Time'] = pd.to_datetime(avax_df['Close Time'] / 1000, unit='s')

avax_num = ['USD', 'Volume', 'Anzahl']
avax_df[trx_num] = avax_df[avax_num].apply(pd.to_numeric, axis=1)

avax_df['Währung'] = "Avalanche (AVAX)"

# Zusammenführung der einzelnen historical Crypto Daten in einen gemeinsamen Dataframe
a = [eth_df, btc_df, bnb_df, ada_df, xrp_df, sol_df, dot_df, doge_df, trx_df, avax_df]
historical_df = pd.concat(a)

# 2.API (für den Header)
response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc")
json_resp = response.json()

crypto_data_df = pd.json_normalize(json_resp)  # dataframe für nicht historical Crypto Info

btc_df1 = crypto_data_df[crypto_data_df['symbol'].str.match('btc')]
eth_df1 = crypto_data_df[crypto_data_df['symbol'].str.match('eth')]
bnb_df1 = crypto_data_df[crypto_data_df['symbol'].str.match('bnb')]
ada_df1 = crypto_data_df[crypto_data_df['symbol'].str.match('ada')]
xrp_df1 = crypto_data_df[crypto_data_df['symbol'].str.match('xrp')]
sol_df1 = crypto_data_df[crypto_data_df['symbol'].str.match('sol')]
dot_df1 = crypto_data_df[crypto_data_df['symbol'].str.match('dot')]
doge_df1 = crypto_data_df[crypto_data_df['symbol'].str.match('doge')]
trx_df1 = crypto_data_df[crypto_data_df['symbol'].str.match('trx')]
avax_df1 = crypto_data_df[crypto_data_df['symbol'].str.match('avax')]

b = [btc_df1, eth_df1, bnb_df1, ada_df1, xrp_df1, sol_df1, dot_df1, doge_df1, trx_df1, avax_df1]
crypto_data_df = pd.concat(b)

crypto_data_df.drop(crypto_data_df.columns[[0, 2, 3, 7, 8, 11, 13, 14, 15, 16, 17,  # droppen von Daten
                                            21, 22, 23, 24, 25, 26, 27, 28]], axis=1,
                    inplace=True)  # die wir nicht brauchen

crypto_data_df['Währung'] = 'Bitcoin (BTC)'  # adden von Column für spätere Zuordnung

crypto_data_df.loc[crypto_data_df.symbol == 'eth', 'Währung'] = 'Ethereum (ETH)'
crypto_data_df.loc[crypto_data_df.symbol == 'bnb', 'Währung'] = 'Binance Coin (BNB)'
crypto_data_df.loc[crypto_data_df.symbol == 'ada', 'Währung'] = 'Cardano (ADA)'
crypto_data_df.loc[crypto_data_df.symbol == 'xrp', 'Währung'] = 'Ripple (XRP)'
crypto_data_df.loc[crypto_data_df.symbol == 'sol', 'Währung'] = 'Solana (SOL)'
crypto_data_df.loc[crypto_data_df.symbol == 'dot', 'Währung'] = 'Polkadot (DOT)'
crypto_data_df.loc[crypto_data_df.symbol == 'doge', 'Währung'] = 'Dogecoin (DOGE)'
crypto_data_df.loc[crypto_data_df.symbol == 'trx', 'Währung'] = 'Tron (TRX)'
crypto_data_df.loc[crypto_data_df.symbol == 'avax', 'Währung'] = 'Avalanche (AVAX)'

# 3. Average Table
a = historical_df.groupby('Währung')['USD'].mean().astype(float).round(2).reset_index()
b = historical_df.groupby('Währung')['Volume'].mean().astype(int).reset_index()
c = historical_df.groupby('Währung')['Anzahl'].mean().astype(int).reset_index()

avg_df = pd.DataFrame(data=a)
df1 = pd.DataFrame(data=b)
df2 = pd.DataFrame(data=c)

avg_df['Volume'] = df1['Volume']
avg_df['Anzahl'] = df2['Anzahl']

def pd_getApi1():
    return historical_df, avg_df, crypto_data_df
