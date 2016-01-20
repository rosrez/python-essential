#!/bin/python3

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage exceptions.py <filename>")
        exit(1)

    try:
        fh = open(sys.argv[1])
    # specific exception type, there may be multiple except clauses in this section
    except IOError:
        print('Could not open the file.')
    # will print the lines from the file only if open succeeds
    else:
        for line in fh: print(line.strip())

if __name__ == "__main__": main()
