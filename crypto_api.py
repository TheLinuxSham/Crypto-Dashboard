import pandas as pd
import requests
from binance import Client

# imports login data and currency's to look for
import user_data as user_d

# user data given from user_data.py
client = Client(user_d.apikey, user_d.secretkey)
crypto_api_list = user_d.crypto_api_list
json_request_list = user_d.json_request_list

# lists for the loops
historical_df_raw = []
crypto_data_df_raw = []
count_dataframe_raw = []


def remove_characters(string):
    return string.replace(" ", "")


for i in crypto_api_list:
    entity = remove_characters(i.lower())
    entity_df = entity + '_df'
    entity_num = entity + '_num'

    entity = client.get_historical_klines(crypto_api_list[i], Client.KLINE_INTERVAL_1DAY, '1 Jan 2022')
    entity_df = pd.DataFrame(entity)
    entity_df.columns = ['Timestamp', 'Open', 'High', 'Low', 'USD', 'Volume', 'Close Time',
                         'UN1', 'Count', 'UN3', 'UN4', 'UN5']
    entity_df['Timestamp'] = pd.to_datetime(entity_df['Timestamp'] / 1000, unit='s')  # conversion zu passendem Daten-
    entity_df['Close Time'] = pd.to_datetime(entity_df['Close Time'] / 1000, unit='s')  # Typ in Dataframe

    entity_num = ['USD', 'Volume', 'Count']
    entity_df[entity_num] = entity_df[entity_num].apply(pd.to_numeric, axis=1)

    entity_df['Währung'] = i
    historical_df_raw.append(entity_df)

historical_df = pd.concat(historical_df_raw)
historical_df_raw.clear()

# requests data from another api for currency info header
response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc")
json_resp = response.json()
crypto_data_df = pd.json_normalize(json_resp)
# creates a new column in the dataframe for a value we work with later
crypto_data_df['Währung'] = 'NaN'

# loops trough currency's to get info
for i in json_request_list:
    entity = str(i)
    currency_string = json_request_list[entity]
    crypto_data_df.loc[crypto_data_df.symbol == entity, 'Währung'] = currency_string
    entity = crypto_data_df[crypto_data_df['symbol'].str.match(entity)]
    crypto_data_df_raw.append(entity)

# merges dataframes and clears old data that's no longer needed
crypto_data_df = pd.concat(crypto_data_df_raw)
crypto_data_df_raw.clear()
crypto_data_df.drop(crypto_data_df.columns[[0, 2, 3, 7, 8, 11, 13, 14, 15, 16, 17,
                                            21, 22, 23, 24, 25, 26, 27, 28]], axis=1,
                    inplace=True)

# creates average tables for the currency's on dashboard
historical_df_raw = historical_df.groupby('Währung')['USD'].mean().astype(float).round(2).reset_index()
crypto_data_df_raw = historical_df.groupby('Währung')['Volume'].mean().astype(int).reset_index()
count_dataframe_raw = historical_df.groupby('Währung')['Count'].mean().astype(int).reset_index()

average_dataframe = pd.DataFrame(data=historical_df_raw)
volume_dataframe = pd.DataFrame(data=crypto_data_df_raw)
count_dataframe = pd.DataFrame(data=count_dataframe_raw)

average_dataframe['Volume'] = volume_dataframe['Volume']
average_dataframe['Count'] = count_dataframe['Count']


# method to return the dataframe to main
def get_crypto_dataframes():
    return historical_df, average_dataframe, crypto_data_df
