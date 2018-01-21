#!/usr/bin/env python3

"""
Python command line tool for taking command of your crypto coins
Command line tool to fetch and display information from the coinmarketcap API
"""

import argparse
import os
import time

from modules import API
from modules import Displayer

__author__ = "Jasper Haasdijk"
__version__ = "0.0.1"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("-c", help="convert to your preferred fiat currency", choices=API.currencies, default="USD",
                        metavar="currency")
    parser.add_argument("-f", help="only display your desired coins", default=None, metavar="list")
    parser.add_argument("-r", help="automatically refresh information every <rate> seconds", default=0, metavar="rate")
    parser.add_argument("-t", help="display the first <top> currencies", default=10, metavar="top")
    args = parser.parse_args()

    if args.f:  # if we are focusing on a specific coin, we want to look further than the top 10 listings
        args.t = 0

    default_iteration(args.t, args.c, args.f, args.r)


def default_iteration(top, convert, find, refresh):
    response = API.get_response(top, convert)
    data = API.parse_response(response)
    output = Displayer.display_information(data, convert.lower(), find)
    print(output)

    while refresh:
        os.system('cls' if os.name == 'nt' else 'clear')
        default_iteration(top, convert, find, refresh=False)
        time.sleep(float(refresh))


if __name__ == '__main__':
    parse_args()
