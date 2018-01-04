import json
import requests

COINS = {'bitcoin': 14446.100, 'ethereum': 719.441, 'bitcoin-cash': 2609.576, 'iota': 3.412, 'dash': 1101.123,
         'monero': 373.981, 'qtum': 53.074, 'stellar': 0.201844, 'zcash': 508.914, 'raiblocks': 10.7311,
         'omisego': 13.495, 'waves': 12.353, 'populous': 30.229, 'salt': 13.756, 'decred': 88.273,
         'maidsafecoin': 0.920078}
INVESTMENT, TOTAL = 1000, 0

response = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=0')
if response.ok:
    data = json.loads(response.content)
    for key in data:
        for name, value in COINS.items():
            if key['id'] == name:
                TOTAL += (float(key['price_usd']) / value) * (INVESTMENT / len(COINS))
    print("{} USD".format(TOTAL))
else:
    myResponse.raise_for_status()
