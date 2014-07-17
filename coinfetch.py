#!/usr/bin/python

# Wow such python
# Feel free to modify
# So generous: DGSWzqyofHC6YDSA34hwVQpWGQHnzJm1sk
#
# Remember to make this file executable ( "$chmod +x ./coinfetch" )

import requests

def findthatcoin(coin):
	"""
	Fetch a coin
	"""
	url = 'http://data.bter.com/api/1/tickers'
	r = requests.get(url)
	out = r.json()[coin]['avg']
	return out

while True:
	coin = raw_input("Which coin? ")
	try:
		price = findthatcoin(coin)
		print price
	except KeyError:
		print "String not found, try swapping the coins around?"
