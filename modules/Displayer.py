#!/usr/bin/env python3

"""
Module which does everything printing
Responsible for the actual output to the console
"""

from tabulate import tabulate


def display_information(data, top=10):
    """ Prints the top x coins, by default top 10 """
    headers = ["Rank", "Coin",
               "Price (USD)", "Market Cap (USD)", "Change (24H)", "Change (7D)"]
    table = []

    for i, key in enumerate(data):
        row = []
        if i == top:
            break
        row.append(i + 1)
        row.append(key['symbol'])
        row.append(key['price_usd'])
        row.append(key['market_cap_usd'])

        if float(key['percent_change_24h']) < 0:
            row.append("\033[1;31;40m{}%\033[0;37;40m"
                       .format(key['percent_change_24h']))
        else:
            row.append("\033[1;32;40m{}%\033[0;37;40m"
                       .format(key['percent_change_24h']))

        if float(key['percent_change_7d']) < 0:
            row.append("\033[1;31;40m{}%\033[0;37;40m"
                       .format(key['percent_change_7d']))
        else:
            row.append("\033[1;32;40m{}%\033[0;37;40m"
                       .format(key['percent_change_7d']))

        table.append(row)

    output = (tabulate(table, headers, floatfmt=(".0f", ".0f", ".4f",
                                                 ".0f", ".2f", ".2f"), tablefmt="fancy_grid"))

    return output
