#!/usr/bin/env python3

"""
Python command line tool for taking command of your crypto coins

Command line tool to:
    - Fetch information from the coinmarketcap API
    - Check how much money you currently have invested in cryptocurrency
"""

import json
import requests

__author__ = "Jasper Haasdijk"
__version__ = "0.0.1"
__status__ = "Alpha"

coins = {'bitcoin': 14446.100, 'ethereum': 719.441, 'bitcoin-cash': 2609.576, 'iota': 3.412, 'dash': 1101.123,
         'monero': 373.981, 'qtum': 53.074, 'stellar': 0.201844, 'zcash': 508.914, 'raiblocks': 10.7311,
         'omisego': 13.495, 'waves': 12.353, 'populous': 30.229, 'salt': 13.756, 'decred': 88.273,
         'maidsafecoin': 0.920078}


def get_response():
    url = 'https://api.coinmarketcap.com/v1/ticker/?limit=0'
    return requests.get(url)


def parse_response(response):
    if response.ok:  # response code is ok (200)
        data = json.loads(response.content)
        return data

    else:  # response code is not ok (200)
        response.raise_for_status()  # print the resulting http error code with description


def check_investment(data):
    investment, total = 1000, 0
    for key in data:
        for name, value in coins.items():
            if key['id'] == name:
                total += (float(key['price_usd']) / value) * \
                    (investment / len(coins))
    return total


if __name__ == '__main__':
    response = get_response()
    data = parse_response(response)
    total = check_investment(data)
    print("{} USD".format(total))
