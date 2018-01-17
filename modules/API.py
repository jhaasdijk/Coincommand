#!/usr/bin/env python3

"""
Module which handles every interaction with the coinmarketcap API
This module fetches data based on the user's request
"""

import json
import sys
from datetime import datetime

import requests

currencies = ["AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP",
              "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK",
              "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD",
              "USD", "ZAR"]


def get_response(top, convert):
    if convert:
        if convert in currencies:
            url = f"https://api.coinmarketcap.com/v1/ticker/?convert={convert}&limit={top}"
        else:
            print("Error: Not a valid currency format")
            sys.exit(1)
    else:
        url = f"https://api.coinmarketcap.com/v1/ticker/?limit={top}"

    date = datetime.now().time()
    print(f"Fetched data from coinmarketcap.com at {date}")

    return requests.get(url)


def parse_response(response):
    if response.ok:  # response code is ok (200)
        data = json.loads(response.content)
        return data

    else:  # response code is not ok (200)
        response.raise_for_status()  # print the resulting http error code with description
