#!/usr/bin/python3

# Wow such python
# Feel free to modify
# So generous: DGSWzqyofHC6YDSA34hwVQpWGQHnzJm1sk
#
# Remember to make this file executable ( "$chmod +x ./dogefetch1" )
#
# To add other coins, use the template below, and modify the coinget
# function accordingly.
#
###########################################################
#
# def <function name>():
#	url = '<http://data.bter.com/api/1/ticker/*>'
#	r = requests.get(url)
#	out = r.json()['avg']
#	return out
#
#############################################################

import requests, sys

def doge_usd():
	"""
	Fetch USD - DOGE
	"""
	url = 'http://data.bter.com/api/1/ticker/doge_usd'
	r = requests.get(url)
	out = r.json()['avg']
	return out
	
def btc_usd():
	"""
	Fetch USD - BTC
	"""
	url = 'http://data.bter.com/api/1/ticker/btc_usd'
	r = requests.get(url)
	out = r.json()['avg']
	return out

def ltc_usd():
	"""
	Fetch LTC - USD
	"""
	url = 'http://data.bter.com/api/1/ticker/ltc_usd'
	r = requests.get(url)
	out = r.json()['avg']
	return out

def coinget(coin):
	"""
	l 	-	ltc
	b 	-	btc
	wow -	doge
	all -	all
	"""
	if coin == "l":
		print ("$"+str(ltc_usd()))
	elif coin == "lwow" or coin == "wowl":
		print ("LTC: $"+str(ltc_usd())+" DOGE: $"+str(doge_usd()))
	elif coin == "lb" or coin == "bl":
		print ("BTC: $"+str(btc_usd())+" LTC: $"+str(ltc_usd()))
	elif coin == "b":
		print ('$'+str(btc_usd()))
	elif coin == "bwow" or coin == "wowb":
		print ("BTC: $"+str(btc_usd())+" DOGE: $"+str(doge_usd()))
	elif coin == "wow":
		print ('$'+str(doge_usd()))
	elif coin == "all":
		print ("BTC: $"+str(btc_usd())+" LTC: $"+str(ltc_usd())+" DOGE: $"+str(doge_usd()))
	else:
		exit("Invalid input")

try:
	coinget(sys.argv[1])
except IndexError:
	exit("Enter an argument!! < b, l, wow, all >")

