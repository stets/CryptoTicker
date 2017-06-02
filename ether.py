#!/usr/bin/env python

import requests

def getPrice():
	response = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/')
	data = response.json()
	data = data[0]
	price = data['price_usd']

	return price

#print data['id'] + " is pretty cool"
#print "It is currently priced at " + data['price_usd']  + " US dollars"
