#!/usr/bin/env python3

"""
Python command line tool for taking command of your crypto coins

Command line tool to:
    - Fetch and display information from the coinmarketcap API
    - Check how much money you currently have invested in cryptocurrency
"""

import argparse
import json
import sys

import requests

from tabulate import tabulate

__author__ = "Jasper Haasdijk"
__version__ = "0.0.1"
__status__ = "Alpha"

"""
List elements consist of ('coin_id', value_when_invested, investment)
Therefore ('bitcoin', 14446.100, 50) means that you invested in bitcoin when the price was 14446.100 with 50 dollars
"""
coins = [('bitcoin', 14446.100, 50), ('ethereum', 719.441, 50),
         ('bitcoin-cash', 2609.576, 50), ('iota', 3.412, 200),
         ('dash', 1101.123, 30), ('monero', 373.981, 100), ('qtum', 53.074, 50),
         ('stellar', 0.201844, 50), ('zcash', 508.914, 50),
         ('raiblocks', 10.7311, 100), ('omisego', 13.495, 50),
         ('waves', 12.353, 50), ('populous', 30.229, 50), ('salt', 13.756, 40),
         ('decred', 88.273, 30), ('maidsafecoin', 0.920078, 50)]


def parse_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--version", help="display version information",
                       action="store_true")
    args = parser.parse_args()

    if args.version:
        print("Coincommand {}".format(__version__))


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
    total = 0
    for key in data:
        for name, value, investment in coins:
            if key['id'] == name:
                total += (float(key['price_usd']) / value) * investment
    return total


def display_information(data, top=10):
    """ Prints the top x coins, by default top 10 """
    headers = ["Rank", "Coin",
               "Price (USD)", "Market Cap (USD)", "Change (24H)", "Change (7D)"]
    table = []
    for i, key in enumerate(data):
        if i == top:
            break
        table.append((i + 1,
                      key['symbol'],
                      key['price_usd'],
                      key['market_cap_usd'],
                      "{}%".format(key['percent_change_24h']),
                      "{}%".format(key['percent_change_7d'])))

    print(tabulate(table, headers, floatfmt=(".1f", ".1f", ".1f",
                                             ".4f", ".1f", ".2f", ".2f", ".2f"), tablefmt="fancy_grid"))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        parse_args()
    else:
        response = get_response()
        data = parse_response(response)
        display_information(data)
        # total = check_investment(data)
        # print("{} USD".format(total))
