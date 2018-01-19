#!/usr/bin/env python3

"""
Python command line tool for taking command of your crypto coins

Command line tool to:
    - Fetch and display information from the coinmarketcap API
"""

# TODO: -- properly mutually exclude -v flag from the rest

import argparse
import os
import time

from modules import API
from modules import Displayer

__author__ = "Jasper Haasdijk"
__version__ = "0.0.1"
__status__ = "Alpha"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="display version information and exit", action="store_true")
    parser.add_argument("-c", help="convert to your preferred fiat currency", choices=API.currencies, default="USD",
                        metavar="currency")
    parser.add_argument("-f", help="only display your desired coins", default=None, metavar="list")
    parser.add_argument("-r", help="automatically refresh information every <rate> seconds", default=0, metavar="rate")
    parser.add_argument("-t", help="display the first <top> currencies", default=0, metavar="top")
    args = parser.parse_args()

    if args.version:
        print(f"Coincommand {__version__}")
        parser.exit(status=0)
    else:
        default_iteration(top=args.t, convert=args.c, find=args.f, refresh=args.r)


def default_iteration(top, convert, find, refresh):
    response = API.get_response(top, convert)
    data = API.parse_response(response)
    currency = convert.lower()
    output = Displayer.display_information(data, currency, find)
    print(output)

    if refresh:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            default_iteration(top, convert, find, refresh=0)
            time.sleep(float(refresh))


if __name__ == '__main__':
    parse_args()
