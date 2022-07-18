#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if True:
            print("{:d}".format(value))
            print('')
    except ValueError:
        print("{} is not an integer".format(value))
