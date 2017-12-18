# CryptoWorth
Very small and easy script to output your entire cryptocurrency portfolio in USD using the API from CoinMarketCap.com

**Remember**: if you want to add coins to the `balances.json` file, make sure the `key` in the dictionary corresponds to the `id` given to it by CoinMarketCap.com. For example the key for BTC is `bitcoin` because the API endpoint for CoinMarketCap is `https://api.coinmarketcap.com/v1/ticker/bitcoin/`.

Run `install.sh` (maybe with sudo) and then `source ~/.bashrc` to activate it in the current shell.

**Just type `worth` into your terminal anytime you feel the itch coming back.**
