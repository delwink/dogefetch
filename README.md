dogefetch
=========

dogefetch:
A dogecoin price fetcher written in python (all output is in USD).

coinfetch:
A python script that is capable of printing almost all cryptocoin prices in terms 
of other coins (and fiat money).

Using dogefetch
---------------

dogefetch takes one argument from the command line:

'wow' fetches the price of DOGE.

'l' fetches the price of LTC.

'b' fetches the price of BTC.

'all' fetches the prices of LTC, BTC and DOGE.

It is possible to fetch two values. For example, lwow will return the prices of both
LTC and DOGE.

Example: <code>$ dogefetch bl</code>

Using coinfetch
---------------

coinfetch takes two arguments from the command line, and returns a conversion factor.

The arguments are the three (or sometimes four) letter identifiers of various currencies.

Many (but not all) pairs of coins can be used.

Example: <code>$ coinfetch doge btc</code>

The above example will return the amount of Bitcoin that can currently be bought with one
Dogecoin. 

If the coins are reversed (e.g. 'coinfetch btc doge' ), the amount of Dogecoin
that can currently be bought with one Bitcoin will be returned.

Installation
------------

To install dogefetch:

<code>$ chmod +x ./dogefetch && sudo cp ./dogefetch /usr/local/bin/</code>

To install coinfetch:

<code>$ chmod +x ./coinfetch && sudo cp ./coinfetch /usr/local/bin/</code>

Licensing
---------

This script is [free software](http://gnu.org/philosophy/free-sw.html), licensed
under the terms of the MIT license. See [LICENSE](LICENSE) for more information.
