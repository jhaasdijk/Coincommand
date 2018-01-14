# Coincommand

```python
__author__ = "Jasper Haasdijk"
__version__ = "0.0.1"
__status__ = "Alpha"
```

Python command line tool for taking command of your crypto coins<br>
Uses the [coinmarketcap](https://coinmarketcap.com/api/) API<br>

Run the script with the `-r` or `--refresh` parameter if you wish to automatically refresh the information every 20 minutes

### Dependencies

- [python-tabulate](https://bitbucket.org/astanin/python-tabulate)

--------------------------------------------------------------------------------

### Completed

- [x] When run without any options, Coincommand will display statistics about the current top 10 listings
- [x] Added colours to make the displayed statistics nicer on the eyes
- [x] Added optional command line parameters for tuning the program to the user's desired use case
  - [x] `-h` `--help` for displaying help information
  - [x] `-v` `--version` for displaying version information
  - [x] `-r` `--refresh` for automatically refreshing the information


### TODO

- [ ] Add clear `README` instructions for how to run the program
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
