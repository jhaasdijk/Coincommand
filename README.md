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

- Show the currently installed version by using the `-v` or `--version` parameter
- Automatically refresh the information every 20 minutes by using the `-r` or `--refresh` parameter
- Get help on the usage of command line flags with the `-h` or `--help` parameter

```
usage: main.py [-h] [-v | -r]

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  display version information
  -r, --refresh  automatically refresh information
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
  - [ ] `-c` for displaying specific coin(s)
  - [ ] `-?` for displaying specific information
  - [ ] etc..
- [ ] Add the option to output to different fiat currencies
- [ ] Add visual aid output. Inspiration taken from [gtop](https://github.com/aksakalli/gtop) and [blessed](https://github.com/yaronn/blessed-contrib)
- [ ] Add the option to load from json format to make use of a user specified configuration
- [ ] Add the option to have user specified alerts as per their configuration
- [ ] Read up on a license and add a license
- [ ] Read up on releasing and add a release

--------------------------------------------------------------------------------
