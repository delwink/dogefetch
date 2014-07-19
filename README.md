dogefetch
=========

See [INSTALL](INSTALL) for installation instructions.

Using `dogefetch`
-----------------

`dogefetch` takes one argument from the command line:

`wow` gets the price of Dogecoin.

`l` gets the price of Litecoin.

`b` gets the price of Bitcoin.

`all` gets the price of Dogecoin, Litecoin, and Bitcoin.

These can also be obtained in pairs. For example, `lb` gets the price of both
Bitcoin and Litecoin.

Example: `$ dogefetch lwow`

Using `coinfetch`
-----------------

coinfetch takes two arguments from the command line, and returns a conversion 
factor.

The arguments are the three (or sometimes four) letter identifiers of various 
currencies.

Many (but not all) pairs of coins can be used.

Example: `$ coinfetch doge btc`

The above example will return the amount of Bitcoin that can currently be bought
with one Dogecoin. 

If the coins are reversed (e.g. `$ coinfetch btc doge`), the amount of Dogecoin
that can currently be bought with one Bitcoin will be returned.

Licensing
---------

This script is [free software](http://gnu.org/philosophy/free-sw.html), licensed
under the terms of the MIT license. See [LICENSE](LICENSE) for more information.
