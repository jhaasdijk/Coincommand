#!/usr/bin/env python3

"""
Module which does everything printing
Responsible for the actual output to the console
"""

from tabulate import tabulate


class Colours:
    GREEN = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'


def populate_table(i, key, table, currency):
    if currency:
        row = [i + 1, key['symbol'], key[f'price_{currency}'],
               key[f'market_cap_{currency}']]
    else:
        row = [i + 1, key['symbol'], key['price_usd'], key['market_cap_usd']]

    if float(key['percent_change_24h']) < 0:
        row.append(Colours.RED + f"{key['percent_change_24h']}%" + Colours.END)
    else:
        row.append(Colours.GREEN + f"{key['percent_change_24h']}%" + Colours.END)

    if float(key['percent_change_7d']) < 0:
        row.append(Colours.RED + f"{key['percent_change_7d']}%" + Colours.END)
    else:
        row.append(Colours.GREEN + f"{key['percent_change_7d']}%" + Colours.END)

    table.append(row)


def display_information(data, currency, find):
    headers = ["Rank", "Coin",
               "Price", "Market Cap", "Change (24H)", "Change (7D)"]
    table = []

    for i, key, in enumerate(data):
        if find:
            if key['symbol'] in find:
                populate_table(i, key, table, currency)
        else:
            populate_table(i, key, table, currency)

    output = (tabulate(table, headers, floatfmt=(".0f", ".0f", ".4f",
                                                 ".0f", ".2f", ".2f"), tablefmt="fancy_grid"))
    return output
