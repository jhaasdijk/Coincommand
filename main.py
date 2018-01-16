#!/usr/bin/env python3

"""
Python command line tool for taking command of your crypto coins

Command line tool to:
    - Fetch and display information from the coinmarketcap API
    - Check how much money you currently have invested in cryptocurrency
"""

# TODO: Colouring
# TODO: -- check colours output in different terminals with different colouring
# TODO: -- properly do the colouring in the printing function

# TODO: Parsing
# TODO: -- optimize argument parser

import argparse
import os
import sys
import time

from modules import API
from modules import Displayer

__author__ = "Jasper Haasdijk"
__version__ = "0.0.1"
__status__ = "Alpha"


def parse_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--version", help="display version information", action="store_true")
    group.add_argument("-c", help="convert to your preferred fiat currency", metavar="currency")
    group.add_argument("-f", help="only display your desired coins", metavar="list")
    group.add_argument("-r", help="automatically refresh information every <rate> seconds", metavar="rate")
    group.add_argument("-t", help="display the first <top> currencies", metavar="top")
    args = parser.parse_args()

    if args.version:
        print("Coincommand {}".format(__version__))

    if args.c:
        default_iteration(convert=str(args.c))

    if args.f:
        wordlist = str(args.f).split(', ')
        default_iteration(top=0, find=wordlist)

    if args.r:
        while True:
            os.system('clear')
            default_iteration()
            time.sleep(float(args.r))

    if args.t:
        default_iteration(top=args.t)


def default_iteration(top=10, convert="", find=None):
    if find is None:
        find = []

    response = API.get_response(top, convert)
    data = API.parse_response(response)
    currency = convert.lower()
    output = Displayer.display_information(data, currency, find)
    print(output)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        parse_args()
    else:
        default_iteration()
