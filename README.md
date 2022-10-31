# Crypto-Dashboard

## What is the Crypto-Dashboard?
The Crypto-Dashboard was a small universitary project to get a feel for python. It uses different APIs to collect data for various crypto currencys. The data includes current prices, trends, trades as well as Twitters latest Tweets about the cryptos and a sentiment analyse. It uses Plotly to create a website and show you all the Info. Featured currencys are:  
* btc, eth, bnb, ada, xrp, sol, dot, doge, trx, avax  
  
> You will need a Twitter development account to run the program with your login credentials!
  
## Technologies
The program uses python to function. You can download python [here](https://www.python.org/downloads/).  
You might also want to check for pip installation with following command in your terminal. If pip is missing you can check this [documentary](https://pip.pypa.io/en/stable/installation/).  
```
pip3 --version
``` 

## The Setup

This program relies on different libraries to run. There's a *requierements.txt* in the folder you can open to see which they are. To install them, run this command when you're inside the directory
```
pip install -r requirements.txt
```
You will also need to change login credentials in *SentimentAnalyse.py* line 7-10 and in *TwitterApi.py* line 7-10.
