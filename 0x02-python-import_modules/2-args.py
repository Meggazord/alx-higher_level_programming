#!/usr/bin/python3

import sys

args = sys.argv[1:]
args_count = len(args)

if not args:
    print("0 arguments.")
else:
    print("{} {}:".format(args_count, 'argument' if args_count < 2 else 'arguments'))
    for i, arg in enumerate(args, 1):
        print("{}: {}".format(i, arg))
