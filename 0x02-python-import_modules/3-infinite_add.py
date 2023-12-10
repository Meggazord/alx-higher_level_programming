#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    args_count = len(args)
    total = 0
    for i in args:
        total += int(i)
    print("{}".format(total))
