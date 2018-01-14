#!/usr/bin/env python3

"""
Module which contains the individual functions
This module holds the main functionality of the script
"""

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


def check_investment(data):
    total = 0
    for key in data:
        for name, value, investment in coins:
            if key['id'] == name:
                total += (float(key['price_usd']) / value) * investment
    return total
