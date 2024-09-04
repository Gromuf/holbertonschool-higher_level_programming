#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    num = len(arguments)

    if num == 0:
        print("0 arguments.")
    elif num == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num))

    for index, arg in enumerate(arguments, start=1):
        print("{}: {}".format(index, arg))
