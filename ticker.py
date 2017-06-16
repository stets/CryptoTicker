#/usr/bin/env python

import requests

def getPrice():
	r = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/')
	data = r.json()[0]
	return data['price_usd'], data['symbol'] 

