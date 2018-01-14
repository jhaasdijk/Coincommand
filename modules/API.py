#!/usr/bin/env python3

"""
Module which handles every interaction with the coinmarketcap API
This module fetches data based on the user's request
"""

import json

import requests


def get_response():
    url = 'https://api.coinmarketcap.com/v1/ticker/?limit=0'
    return requests.get(url)


def parse_response(response):
    if response.ok:  # response code is ok (200)
        data = json.loads(response.content)
        return data

    else:  # response code is not ok (200)
        response.raise_for_status()  # print the resulting http error code with description
