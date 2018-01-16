# Coincommand

```python
__author__ = "Jasper Haasdijk"
__version__ = "0.0.1"
__status__ = "Alpha"
```

Python command line tool for taking command of your crypto coins<br>
Uses the [coinmarketcap](https://coinmarketcap.com/api/) API<br>

## Introduction

Quickly check current crypto statistics from the ease of your terminal<br>
Some of the current features include:

- Get help on the usage of command line flags with the `-h` or `--help` parameter
- Show the currently installed version by using the `-v` or `--version` parameter
- Convert to your preferred fiat currency by using the `-c` or `--convert` flag. Valid values are:
- Automatically refresh the information every `rate` seconds by using the `-r` or parameter

```
"AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP",
"HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK",
"NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD",
"USD", "ZAR"
```

```
usage: main.py [-h] [-v | -c currency | -r rate]

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  display version information
  -c currency    convert to your preferred fiat currency
  -r rate        automatically refresh information every <rate> seconds
```

- Display information about the current top 10 listings by running the tool without any options. This is the default behaviour
- Terminal colours to make the displayed statistics nicer on the eyes

## Getting started

Install dependency `python-tabulate`
```
$ pip install tabulate
```

Clone this repository at the desired location
```
$ git clone https://github.com/jhaasdijk/Coincommand.git
```

Move into the `Coincommand` folder
```
$ cd Coincommand
```

Run the utility
```
$ python3 main.py
```

## Dependencies

- python3
- [python-tabulate](https://bitbucket.org/astanin/python-tabulate)

## Troubleshooting

If you run into any errors, please do not hesitate to create an issue

--------------------------------------------------------------------------------

## TODO

- [ ] Add optional command line parameters for tuning the program to the user's desired use case
  - [ ] `-d` for displaying specific coin(s)
  - [ ] `-?` for displaying specific information
  - [ ] etc..
- [ ] Add visual aid output. Inspiration taken from [gtop](https://github.com/aksakalli/gtop) and [blessed](https://github.com/yaronn/blessed-contrib)
- [ ] Add the option to load from json format to make use of a user specified configuration
- [ ] Add the option to have user specified alerts as per their configuration

--------------------------------------------------------------------------------
