#!/bin/python3

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage exceptions.py <filename>")
        exit(1)

    try:
        fh = open(sys.argv[1])
        # will print the lines from the file only if open succeeds:
        # we don't need the else clause
        for line in fh: print(line.strip())
    except IOError as e:
        print('Could not open the file:', e)

    # again, multiple except clauses may follow for different exception types

if __name__ == "__main__": main()
