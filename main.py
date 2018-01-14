#!/usr/bin/env python3

"""
Python command line tool for taking command of your crypto coins

Command line tool to:
    - Fetch and display information from the coinmarketcap API
    - Check how much money you currently have invested in cryptocurrency
"""

# TODO: add check on which system it is running (check os.name)
# TODO: add option with the -r flag for delay when to refresh
# TODO: check colours output in different terminals with different colouring
# TODO: properly do the colouring in the printing function
# TODO: explore other options for command line parameters than argparse

import argparse
import os
import sys
import time
from datetime import datetime

from modules import API
from modules import Displayer

__author__ = "Jasper Haasdijk"
__version__ = "0.0.1"
__status__ = "Alpha"


def parse_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--version", help="display version information",
                       action="store_true")
    group.add_argument("-r", "--refresh",
                       help="automatically refresh information", action="store_true")
    args = parser.parse_args()

    if args.version:
        print("Coincommand {}".format(__version__))

    if args.refresh:
        while True:
            os.system('clear')
            default_iteration()
            time.sleep(1200)  # refreshes every 20 minutes


def default_iteration():
    date = datetime.now().time()
    print("Fetched data from coinmarketcap.com at {}".format(date))
    response = API.get_response()
    data = API.parse_response(response)
    output = Displayer.display_information(data)
    print(output)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        parse_args()
    else:
        default_iteration()
